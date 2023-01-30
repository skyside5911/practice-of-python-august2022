<?php
    /**
    * Plugin Name: Category Author Auto Assign
    * Plugin URI: https://facebook.com/jaydeep.gajera
    * Description: Personal Plugin
    * Version: 1.0
    * Author: Jaydeep Gajera
    * Author URI: https://facebook.com/jaydeep.gajera
    **/


    /*--- Plugin Activation Hook ---*/
    if (!class_exists("CAAA")) {
        class CAAA {

            public function __construct() {
                register_activation_hook( __FILE__, array($this,'create_table'));
                register_deactivation_hook( __FILE__, array($this,'drop_table') );

                add_action('admin_menu', array($this, 'setup_menu'));
                add_action('wp_ajax_upsert_caa',array($this,'upsert_caa'));
                add_filter('wp_insert_post_data', array($this, 'wp_set_category_author_assign'), '', 2);
                add_action('add_meta_boxes', array($this, 'add_meta_boxes'));
                add_action('admin_footer', array($this, 'title_format') );
                global $wpdb; 
                $this->$db_table_name = $wpdb->prefix . 'category_author_auto_assign';  // table name
            }

            function create_table(){      
                global $wpdb; 
                $charset_collate = $wpdb->get_charset_collate();

                //Check to see if the table exists already, if not, then create it
                if($wpdb->get_var( "show tables like '".$this->$db_table_name."'" ) != $this->$db_table_name ) 
                {
                    $sql = "CREATE TABLE ".$this->$db_table_name." (
                            id int(11) NOT NULL auto_increment,
                            category_id int(11) NOT NULL,
                            author_id int(11) NOT NULL,
                            PRIMARY KEY (id),
                            UNIQUE KEY (category_id)
                    ) $charset_collate;";

                require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );
                    dbDelta( $sql );
                    add_option( 'caaa_db_version', $test_db_version );
                }
            } 

            function drop_table() {
                global $wpdb;
                $sql = "DROP TABLE IF EXISTS ".$this->$db_table_name;
                $wpdb->query($sql);
                delete_option("caaa_db_version");
            }   

            /*--- Plugin Add Menu ---*/
            function setup_menu(){
                add_menu_page( 'Category Author Auto Assign', 'CAAA', 'manage_options', 'category-author-auto-assign', array($this, 'caaa_admin_page') );
            }

            function add_meta_boxes(){
                add_meta_box('caaa-metabox', 'CAAA', array($this, 'caaa_meta_box'), array('post','page'), 'side', 'core');
            }
            
            public function caaa_admin_page(){
                $form_action = "#";
                $categories = get_categories();
                $authors = get_users();
                global $wpdb;
                $db_category_author_assigns = $wpdb->get_results(
                    "SELECT category_id, author_id FROM ".$this->$db_table_name
                );
                echo "<span id='db-category-author-assign' style='display:none'>" . wp_json_encode($db_category_author_assigns) . "</span>";
                ?>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                <div class="container">
                    <div class="row">
                        <div class="col-md-12">
                            <br/>
                            <h2>Category Author Auto Assign</h2><br/>
                            <div class="alert alert-primary gj-alert" role="alert">
                                Welcome,
                            </div>
                            <form action="<?=$form_action?>">
                                <?php foreach($categories as $category) : ?>
                                    <div class="row">
                                        <div class="col-md-4">
                                            <h4><?=$category->name?></h4>
                                        </div>
                                        <div class="col-md-4">
                                            <div class="form-group">
                                                <select class="form-select caaa" data-category-id="<?=$category->term_id?>" data-category-name="<?=$category->name?>" data-author-name="<?=$author->display_name?>">
                                                    <option value="None">None</option>
                                                    <?php foreach($authors as $author): ?>
                                                        <option value="<?=$author->ID?>"><?=$author->display_name?></option>
                                                    <?php endforeach; ?>
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                <?php endforeach; ?>
                            </form>
                        </div>
                    </div>
                </div>
                <script>
                jQuery(document).ready(function(){

                    var caaa = JSON.parse(jQuery("#db-category-author-assign").html());
                    console.log(caaa);
                    caaa.forEach(function(data, index, arr){
                        jQuery(".gj-alert").html("Loading ... ");
                        var category_id = data.category_id;
                        var author_id = data.author_id;
                        jQuery("[data-category-id='"+category_id+"']").val(author_id);
                        jQuery(".gj-alert").html("Welcome,");
                    });

                    jQuery(".caaa").change(function(){
                        var author_id = jQuery(this).val();
                        var category_id = jQuery(this).data("category-id");
                        var category_name = jQuery(this).data("category-name");
                        var author_name = jQuery(this).data("author-name");
                        jQuery.ajax({
                          type:'POST',
                          data:{action:'upsert_caa', category_id: category_id, author_id: author_id, category_name: category_name, author_name: author_name},
                          url: "<?=site_url("/wp-admin/admin-ajax.php")?>",
                          success: function(data) {
                            // alert(value);
                            data = JSON.parse(data);
                            jQuery(".gj-alert").removeClass("alert-success");
                            jQuery(".gj-alert").removeClass("alert-danger");
                            jQuery(".gj-alert").addClass(data.class);
                            jQuery(".gj-alert").html(data.message);
                          }
                        });
                    });
                });
                </script>
                <?php
            }

            public function upsert_caa(){
                $category_id = $_POST['category_id'];
                $author_id = $_POST['author_id'];
                $category_name = $_POST['category_name'];
                $author_name = $_POST['author_name'];

                global $wpdb;  

                $result = $wpdb->update($this->$db_table_name, 
                    array(
                        'category_id' => $category_id, 
                        'author_id' => $author_id
                    ),
                    array(
                        'category_id' => $category_id
                    ),
                    array( '%d', '%d' ), 
                    array( '%d' )
                );
                if ($result === FALSE || $result < 1) {
                    $result = $wpdb->insert( $this->$db_table_name, 
                        array(
                            'category_id' => $category_id, 
                            'author_id' => $author_id
                        ),
                        array( '%d', '%d' ) 
                    );
                }
                if($result){
                    $data = array();
                    $data['class'] = "alert-success";
                    $data['message'] = $category_name . " is assigned to " . $author_name;
                    echo wp_json_encode($data);
                }else{
                    $data = array();
                    $data['class'] = "alert-danger";
                    $data['message'] = "Error - " . $category_name . " is not assigned to " . $author_name;
                    echo wp_json_encode($data);
                }
                wp_die(); 
            }

            function wp_set_category_author_assign ($data, $postarr){
                // echo "<pre>";
                // var_dump($postarr);
                // echo "</pre>";
                // die();
                $caaa_activate = 0;
                if ($_POST['caaa_activate'] == 1){
                    $caaa_activate = 1;
                    $original_author_id = $author_id = $data['post_author'];
                    $categories = $postarr['post_category'];
                    
                    $original_author_id_meta = get_post_meta( get_the_ID(), 'original_author_id');
                    if(!$original_author_id_meta){
                        add_post_meta(get_the_ID(), "original_author_id", $original_author_id);
                    }
    
                    global $wpdb;
                    $db_category_author_assigns = $wpdb->get_results(
                        "SELECT category_id, author_id FROM ".$this->$db_table_name
                    );
                    foreach($db_category_author_assigns as $dcaa){
                        foreach ($categories as $category_id){
                            if ($category_id == $dcaa->category_id){
                                $author_id = $dcaa->author_id;
                            }
                        }    
                    }
                    
                    $data['post_author'] = $author_id;
                    $postarr['post_author'] = $author_id;
                }
                $caaa_activate_meta = get_post_meta( get_the_ID(), 'caaa_activate');
                if(!$caaa_activate_meta){
                    add_post_meta(get_the_ID(), "caaa_activate", $caaa_activate);
                }else{
                    update_post_meta(get_the_ID(), "caaa_activate", $caaa_activate);
                }                 

                return $data;    
            }

            function caaa_meta_box(){
                $html = '';
                $original_author_id_meta = get_post_meta( get_the_ID(), 'original_author_id');
                if($original_author_id_meta){
                    $original_author_id = $original_author_id_meta[0];
                    $user_data = get_user_meta($original_author_id);
                    $html .= "Original Author : " . $user_data["first_name"][0] . " " . $user_data["last_name"][0] . " (" . $user_data["nickname"][0]. ")<br/>";
                }
                $caaa_activate = 1;
                $caaa_activate_meta = get_post_meta( get_the_ID(), 'caaa_activate');
                if($caaa_activate_meta){
                    $caaa_activate = $caaa_activate_meta[0];
                }                 
                $html .= "CAAA Activate : <input name='caaa_activate' type='checkbox' ".($caaa_activate==1?"checked":"")." value='1' />";
                echo $html;
            }

            function title_format() {
                ?>
                    <script type="text/javascript">
                        jQuery(document).ready(function(){
                            jQuery("[name='post_title']").css("width","90%").after(" <button id='format_title'>Format</button><span id='title_length'></span>");

                            jQuery("#format_title").click(function(event) {
                                var post_title = jQuery("[name='post_title']").val();
                                post_title = post_title.toLowerCase().replace(/\b[a-z]/g, function(letter) {
                                    return letter.toUpperCase();
                                });
                                jQuery("[name='post_title']").val(post_title);
                                event.preventDefault();
                            });

                            jQuery("[name='post_title']").keypress(function(event) {
                                jQuery("#title_length").html((jQuery("[name='post_title']").val()).length);
                            });    
                        });
                    </script>
                <?php
                }
        }
    }
    if (class_exists("CAAA")) {
        $caaa = new CAAA();
    }
