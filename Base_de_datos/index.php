<!DOCTYPE html>
<html>
<head>
  <title>RFID Logs</title>
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
    }
    table, th, td {
      border: 1px solid black;
    }
    th, td {
      padding: 15px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h2>RFID Usage Logs</h2>
  <table>
    <tr>
      <th>ID</th>
      <th>Card ID</th>
      <th>Timestamp</th>
    </tr>
    <?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "rfid_db";

    // Crear conexión
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verificar conexión
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT id, cardID, timestamp FROM rfid_logs ORDER BY timestamp DESC";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
      // Mostrar datos de cada fila
      while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["id"]. "</td><td>" . $row["cardID"]. "</td><td>" . $row["timestamp"]. "</td></tr>";
      }
    } else {
      echo "<tr><td colspan='3'>No logs found</td></tr>";
    }
    $conn->close();
    ?>
  </table>
</body>
</html>
