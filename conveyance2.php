<?php

/** 
 * 	Transfer class for datadesk_workflow
 * 	@author h1tjm03
 * 
 */

//require dirname(__FILE__) . '\logger.php';

class Transfer {
	
	public $user_name;
	public $dir;
	public $files;
	public $file_count;
	public $series_count;
	public $api_key;
	public $release_id;
	public $request;
	public $ch;
	public $download;
	public $expected;
	public $matches;

	//Declare constants for Proxy and Useragent
	const PROXY = "http://h1proxy.frb.org:8080/";
	const USERAGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0";

	/**
	 * 	Constructor function to initialize class and declare variables.
	 *
	 */
	public function __construct() {

		$this->user_name = strtolower(exec("ECHO %USERNAME%", $output_temp, $return_temp));;
		$this->dir = "C:/Users/$this->user_name/Documents/test_directory/"; //$dir
		$this->files = array_diff(scandir($this->dir), array('..', '.'));
		$this->file_count = count($this->files);
		$this->series_count = ($this->file_count)/2;
		$this->api_key = "76bb1186e704598b725af0a27159fdfc";
		$this->release_id = 97; //$release_id;
		//$this->expected_series_count = $expected_series_count;
		$this->request = "http://api.stlouisfed.org/fred/release/series?release_id=$this->release_id&api_key=$this->api_key&file_type=json";
		$this->ch = curl_init();
		$this->download_obj = curl_exec($this->ch);
		$this->expected = NULL;
		$this->matches = NULL;
	}

	/**
	 *	Username getter used for debugging
	 *
	 */
	public function get_username() {

		echo "Username: ".$this->user_name."\n";
	}

	/**
	 *	Directory getter used for debugging
	 *
	 */
	public function get_dir() {

		echo "File Location: ".$this->dir."\n";
	}

/*	public function get_expected_count() {
		
	}
*/
	public function count_files() {

		echo "There are ".$this->file_count." files."."\n";
	}
	
	/**
	 * This function validates the count of series to upload. 
	 * The program errors out if there is only one file or if there are an odd number of files.
	 *
	 */
	public function count_series() {

		if ($this->file_count == 1) 
		{
			echo "Error: There is only one file in the directory. Exiting program.\n";
			//Logging goes here.
			exit;
		} 
		else if ($this->file_count % 2 !== 0) 
		{
			echo "Error: There are an odd number of files in the directory. Exiting program.\n";
			//Delete files from directory
			//Logging goes here.
			exit;
		} 
		else 
		{
			echo "There are ".$this->series_count." series."."\n";
			$this->compare_series();
		}
	}
	
	public function download_json() {

		curl_setopt($this->ch, CURLOPT_URL, $this->request);
		curl_setopt($this->ch, CURLOPT_USERAGENT, Transfer::USERAGENT);
		curl_setopt($this->ch, CURLOPT_RETURNTRANSFER,1);
		curl_setopt($this->ch, CURLOPT_PROXY, Transfer::PROXY);
		
		while (!isset($this->download_obj) || $this->download_obj === false || preg_match("/\<\!DOCTYPE HTML PUBLI/", $this->download_obj)) 
		{
			$this->download_obj = curl_exec($this->ch);
		}
	}	

	public function compare_series() {

		$this->download_json();
		if (!preg_match("/\"count\":(\d*)/", $this->download_obj, $this->matches)) 
		{
			echo "Did not find the series count that is listed in the downloaded file.\n";
			//Logging goes here.
			exit;
		} 
		else 
		{
			$this->expected = $this->matches[1];
			if ($this->expected == $this->series_count) 
			{
				echo "The expected number of series "."(".$this->expected.")"." matches the number of processed series. "."(".$this->series_count.")".".\nProceeding to upload the files to FRED";
				$this->loading_animation();
			} 
			else 
			{
				echo "There is a discrepancy between the number of expected series and the number of series in the directory. Please see the log for details.\n";
				$this->series_different();
				//Logging goes here.
				exit;
			}
		}
	}

	public function series_different() {

		echo $this->expected." does not equal ".$this->series_count."."."\n";
	}

	public function transfer_series() {


	}

	public function compare_transferred() {


	}

	public function file_volume_check () {


	}

	public function success_message() {

		echo "File upload successful.\n";
	}

	public function error_message() {

		echo "Oops. There was an error. Please see the log for details.\n";
	}

	public function die() {

		
	}

	public function loading_animation() {

		for ($seconds = 0; $seconds < 5; $seconds++) 
		{
			print ".";
			sleep(1);
		}
		echo "\n";
	}

	public function json_test() {
		$this->download_json();
		$json = json_decode($this->download_obj);
		if (isset($json)) 
		{
			echo "true\n";
			foreach ($json as $obj) 
			{
				echo $obj."\n";
			}
		} 
		else
		{
			echo "error";
			exit;
		}

	}
/*	public function __destruct() {
		
	}
*/

}

$test = new Transfer();
$test->get_username();
$test->get_dir();
$test->count_files();
$test->count_series();
/*$test->json_test();*/
?>
