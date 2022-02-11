<?php 
$input = file_get_contents("input.txt");
$handle = fopen("input.txt", "r");

if ($handle) {
  $data_array = array();
  $boards_array = array();
  $boards_marks = array();
  $index = 0;

  $index_boards = 1;
  while (($data = fgets($handle)) !== false) {
    $data = preg_replace("/\r|\n/", "", $data);
    $data_array[] = $data;

    if ($index > 1) {
      
      //? if data is not empty
      if (!empty($data)) {
        
        // trim to replace whitespace.
        // str_replace remove double space on single digit
        $data = trim(str_replace("  ", " ", $data), " ");
        // array_map
        $board_array[] = array_map('intval', explode(" ", $data));

        if ($index_boards % 5 == 0) {
          $boards_array[] = $board_array;
          $board_array = [];
        }

        $index_boards++; 
      }
    }
    //? Runs after $index > 1
    $index++;
  }
}

  $draw_numbers = explode(",", $data_array[0]);
  echo $draw_numbers;
 