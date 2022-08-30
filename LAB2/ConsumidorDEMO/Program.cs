using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsumidorDEMO
{
    class Program
    {
        static void Main(string[] args)
        {
            String cola = Convert.ToString(args[0]);
            var factory = new ConnectionFactory() { HostName = "localhost" };
            using (var connection = factory.CreateConnection())
            {
                using(var channel = connection.CreateModel())
                {
                    channel.QueueDeclare(cola, false, false, false, null);
                    var consumer = new QueueingBasicConsumer(channel);
                    channel.BasicConsume(cola, true, consumer);
                    Console.WriteLine(" Esperando los mensajes, Ctrl + c para salir...");
                    Console.WriteLine("Primer dato corresponde a temperatura y segundo corresponde a humedad");
                    while (true) {
                        var ea = (BasicDeliverEventArgs)consumer.Queue.Dequeue();
                        var body = ea.Body;
                        var message = Encoding.UTF8.GetString(body);
                        Console.WriteLine(message);
                    }
                }
            }

        }
    }


}
