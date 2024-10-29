<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $dln = $_POST['dln'];
    $secretPassword = "Password"; // Set your actual secret password here

    if ($dln === "10000") {
        // Only send this back if the DLN is correct
        echo "<script>alert('You have unlocked a secret password: $secretPassword');</script>";
    }
}
?>
