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

  $sql = "SELECT * FROM Book";
  $result = mysqli_query($conn, $sql);
  $select_form_title = '<select name="Bnum">';
  while($row = mysqli_fetch_array($result)){
    $select_form_title .= '<option value="'.$row['Bnum'].'">'.$row['title'].'</option>';
  }
  $select_form_title .= '</select>';


  $sql = "SELECT * FROM User";
  $result = mysqli_query($conn, $sql);
  $select_form = '<select name="ID">';
  while($row = mysqli_fetch_array($result)){
    $select_form .= '<option value="'.$row['ID'].'">'.$row['Name'].'</option>';
  }
  $select_form .= '</select>';
?>
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>도서 리뷰 관리 시스템-생성</title>
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
      </br></br>
      <div id="jb-footer">
          <form action="process_create.php" method="POST">
            <?=$select_form_title?>
            <p><textarea name="Remarks" placeholder="Remarks"></textarea></p>
            <?=$select_form?>
            <p><input type="submit" class="btn"></p>
          </form>
        </div>
    </div>
  </body>
</html>
