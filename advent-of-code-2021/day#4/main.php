	<?php
 class Day4
 {
     public $x;
     public $y;

     public function __construct($argX, $argY)
     {
         $this->x = $argX;
         $this->y = $argY;
     }

     public function parser(){ 

        $first = true;
        $count = 0;
        $bingo_numbers = [];

        $handle = fopen('test.txt','r');

        if($handle){

            $boards_array = array();
            $index = 0;
            $index_boards = 1;

            while ($line = fgets($handle)) {

                $data = preg_match("/\r|\n", "", $data);
                $data_array[] = $data;
                
                if($index > 1){
                    if (!empty($data)){
                        $data = trim(str_replace("  ", " ", $data), " ");

                        $board_array[] = array_map('intval', explode(" ", $data));

                        if($index_boards % 5 == 0){ 
                            $board_array[] = $board_array;
                        }
                        $index_boards++;
                    }
                }

                $index++;


              }
        }
        fclose($handle);
    }
        
    public function horizontalCheck(){

    }

    public function verticalCheck(){

    }

     
 }