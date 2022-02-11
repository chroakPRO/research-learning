<?php
class Solver {
    
    // Functions that are important for parsing.
    /*
        ?? 'strtolower & strtoupper: Makes string upper or lower case
        ?? substr (Imporant): Return part of a string
        ?? chunk_split: Split a string into smaller chunks.
        ?? str_contains: Check if substring can be found inside string.
        ?? Explode: explode string into an array.
        ?? strstr: Find the first occurence of a string
        ?? str_shuffle: Randomly shuffles a string
        ?? strlen: length of string
        ?? strspn: Finds the length of the initial segment of a string consisting entirely of characters contained within a given mask.
        ?? implode: 
        ?? str_split & str_replace
        ?? strrpos:
        ?? trim & ltrim:
    */
    public static function  _strtolower(){
        /**
        * 1. Write a PHP script to
        * a) transform a string all uppercase letters.
        * b) transform a string all lowercase letters.
        * c) make a string's first character uppercase.
        * d) make a string's first character of all the words uppercase.
        */

        $test2 = "hejheSASDj";

        echo strtolower($test2);
    }

    public static function challenge2(){
        
        $str1= '082307'; 
        echo substr(chunk_split($str1, 2, ':'), 0, -1)."\n";

    }

    public static function challenge3(){ 
        $string = "0423456789423456789abcdef";
        $substr = "0423456789";

        if(str_contains($string, $substr) !== false){
            echo "found substr in string";
         }
    }

    public static function challenge4(){ 
        $sample = 'www.example.com/public_html/index.php';

        $x = explode('/', $sample);
        echo $x[count($x)-1];
    }

    public static function challenge6(){ 
        $mailid  = 'rayy@example.com';
        // Find first occurrence
        $user = strstr($mailid, '@', true);
        echo $user."\n";
    }

    public static function challenge7(){ 
        $str1 = 'rayy@example.com';
        echo substr($str1, -3)."\n";
    }

    public static function challenge8(){
        $value1 = 65.45;
        $value2 = 104.35;
        echo sprintf("%1.2f", $value1+$value2)."\n";
    }

    public static function password_generate($chars) {
        $data = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcefghijklmnopqrstuvwxyz';
        return substr(str_shuffle($data), 0, $chars);
    }
    
    public static function challenge9($chars){
  
        echo self::password_generate(7)."\n";
    }

    public static function challenge10(){
        $sample = "the quick brown fox jumps over the lazy dog";
        $count = 0;
        $prased = preg_replace("/the/", "That", $sample, 1);
        echo $prased;
    }

    public static function challenge11(){
        $str_pos = strspn("hek", "hej", "\0");
    }

    public static function challenge12(){

    }

}




Solver::challenge10();
