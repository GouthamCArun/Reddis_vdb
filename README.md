<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redis Project - README</title>
</head>
<body>
    <h1>Redis Project</h1>
    <p>This project demonstrates how to use Redis for storing and retrieving data using Python and C#.</p>

    <h2>Overview</h2>
    <p>Redis is an in-memory data store commonly used for caching and data storage. This project uses Redis to store key-value pairs and retrieve them efficiently.</p>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Redis:</strong> In-memory data store</li>
        <li><strong>Python:</strong> Backend for interacting with Redis</li>
        <li><strong>C#:</strong> Example implementation using StackExchange.Redis</li>
    </ul>

    <h2>How it Works</h2>
    <ol>
        <li><strong>Connect to Redis:</strong> Use the provided credentials (host, port, username, password) to connect to the Redis server.</li>
        <li><strong>Set Data:</strong> Store data in Redis as key-value pairs (e.g., `"foo" = "bar"`).</li>
        <li><strong>Get Data:</strong> Retrieve data from Redis using the key (e.g., retrieve the value associated with the key `"foo"`).</li>
    </ol>

    <h2>Setup Instructions</h2>
    <h3>For Python</h3>
    <p>Install the Redis package using pip:</p>
    <pre><code>pip install redis</code></pre>
    <p>Run the Python script to connect, set, and get data in Redis.</p>

    <h3>For C#</h3>
    <p>Install StackExchange.Redis via NuGet:</p>
    <pre><code>Install-Package StackExchange.Redis</code></pre>
    <p>Run the C# script to interact with Redis.</p>

    <h2>Code Example</h2>
    <h3>Python Example</h3>
    <pre><code>
import redis

# Connect to Redis
r = redis.Redis(host='redis-18436.c282.east-us-mz.azure.redns.redis-cloud.com', port=18436, password='your_password')

# Set and get data
r.set('foo', 'bar')
value = r.get('foo')
print(f'Key: foo, Value: {value.decode()}')
    </code></pre>

    <h3>C# Example</h3>
    <pre><code>
using StackExchange.Redis;

public class RedisExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect(
            new ConfigurationOptions{
                EndPoints = { {"redis-18436.c282.east-us-mz.azure.redns.redis-cloud.com", 18436} },
                User = "default",
                Password = "your_password"
            }
        );
        var db = muxer.GetDatabase();

        // Set and get data
        db.StringSet("foo", "bar");
        RedisValue result = db.StringGet("foo");
        Console.WriteLine($"Key: foo, Value: {result}");
    }
}
    </code></pre>

    <h2>Conclusion</h2>
    <p>This project demonstrates how easy it is to interact with Redis to store and retrieve data using Python and C#. Redis is a powerful tool for fast, in-memory data storage, and this project showcases a basic usage example.</p>
</body>
</html>
