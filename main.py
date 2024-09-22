<html><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Koja-xD WEB / MESSENGER GROUP CHECKER</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
        body {
            background-color: #1a202c;
            color: #f9f9f9;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 800px;
            margin-top: 50px;
        }
        .card {
            margin-bottom: 20px;
            background-color: #2d3748;
            border: 1px solid #4a5568;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .card-body {
            padding: 20px;
        }
        .card-title {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        .form-control {
            display: block;
            width: 100%;
            padding: 0.375rem 0.75rem;
            font-size: 1rem;
            line-height: 1.5;
            color: #f9f9f9;
            background-color: #4a5568;
            background-clip: padding-box;
            border: 1px solid #4a5568;
            border-radius: 0.25rem;
            transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
        }
        .form-control:focus {
            border-color: #eab308;
            outline: none;
            box-shadow: 0 0 0 0.2rem rgba(234, 179, 8, 0.25);
        }
        .btn-group {
            display: flex;
            justify-content: space-between;
        }
        .btn-primary, .btn-secondary, .btn-info, .btn-neon {
            border-radius: 20px;
            font-weight: bold;
        }
        .btn-primary {
            color: #fff;
            background-color: #eab308;
            border-color: #eab308;
            cursor: pointer;
        }
        .btn-primary:hover {
            background-color: #ffcc33;
            border-color: #ffcc33;
        }
        .btn-secondary {
            color: #fff;
            background-color: #6c757d;
            border-color: #6c757d;
            cursor: pointer;
        }
        .btn-secondary:hover {
            background-color: #5a6268;
            border-color: #545b62;
        }
        .btn-info {
            color: #fff;
            background-color: #17a2b8;
            border-color: #17a2b8;
            cursor: pointer;
        }
        .btn-info:hover {
            background-color: #138496;
            border-color: #117a8b;
        }
        .btn-neon {
            color: #fff;
            background-color: #ffcc33;
            border-color: #ffcc33;
            box-shadow: 0 0 10px #ffcc33, 0 0 40px #ffcc33, 0 0 80px #ffcc33;
            transition: all 0.5s ease;
            cursor: pointer;
        }
        .btn-neon:hover {
            box-shadow: 0 0 5px #ffcc33, 0 0 20px #ffcc33, 0 0 40px #ffcc33, 0 0 80px #ffcc33;
        }
    </style>
</head>
<body>
    <div class="container">
        <h3 class="text-center mb-4">MESSENGER GROUP CHECKER</h3>
        <div class="card">
            <div class="card-body">
                <h2 class="card-title">Enter Your Facebook Access Token</h2>
                <form id="form" method="post">
                    <div class="form-group">
                        <label for="access_token">ACCESS TOKEN:</label>
                        <input type="text" class="form-control" id="access_token" name="access_token" required="">
                    </div>
                    <div class="btn-group">
                        <button type="submit" formaction="/get_groups" class="btn btn-neon mt-3">GET GROUPS</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

</body></html>
