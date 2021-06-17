<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">


<?php
$conn = mysqli_connect(
  'localhost',
  'root',
  'qwerty1234',
  'bookreview');

$sql = "SELECT * from bookreport p left join book b on p.Bnum=b.Bnum order by p.bnum";
$result = mysqli_query($conn, $sql);
$list = '';
while($row = mysqli_fetch_array($result)) {
  $escaped_title = htmlspecialchars($row['title']);
  $list = $list."<li><a href=\"index.php?Pid={$row['Pid']}\">{$escaped_title}</a></li>";
}

$article = array(
  'title'=> 'WEB',
  'Remarks'=>'Hello, web'
);

$update_link = '';
if(isset($_GET['Pid'])) {
  $filtered_id = mysqli_real_escape_string($conn, $_GET['Pid']);
  $sql = "SELECT * from bookreport p left join book b on p.Bnum=b.Bnum where Pid={$filtered_id}";
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_array($result);
  $article['title'] = htmlspecialchars($row['title']);
  $article['Remarks'] = htmlspecialchars($row['Remarks']);
  $update_link = '<a href="update.php?Pid='.$_GET['Pid'].'">update</a>';
}
?>


<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>도서 리뷰 관리 시스템 - 수정</title>
    <link rel="stylesheet" href="main.css">
  </head>
  <body>
    <div id='jb-container'>
      <div id='jb-header'><h1><a href="index.php">도서 관리 시스템</a></h1></div>
      <div id="jb-footer" style="overflow:auto; height:300px;">
        <ol class="mylist">
          <?=$list?>
        </ol>
      </div>
      </br>
      <div id="jb-footer">
        <form action="process_update.php" method="POST">
          <input type="hidden" name="Pid" value="<?=$_GET['Pid']?>">
          <p>변경하고자 하는 리뷰의 책 제목 : <b><?=$article['title']?></b></p>
          <p><textarea name="Remarks" placeholder="Remarks"><?=$article['Remarks']?></textarea></p>
          <p><input type="submit" class="btn"></p>
        </form>
      </div>
    </div>
  </body>
</html>
