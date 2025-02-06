using System;
using System.Threading.Tasks;
using Playwright;

class Program
{
    static async Task Main(string[] args)
    {
        using var playwright = await Playwright.CreateAsync();
        await using var browser = await playwright.Chromium.LaunchAsync(headless: false); // Set headless to true for background execution
        var page = await browser.NewPageAsync();

        // Login to Airflow
        await page.GotoAsync("https://airflow.com");
        await page.FillAsync("#username", "ffm");
        await page.FillAsync("#password", "ffm1");
        await page.ClickAsync("button[type=submit]");
        await page.WaitForSelectorAsync("#trigger_dag"); // Wait for login success

        // Schedule the DAG run at 00:00 every day
        while (true)
        {
            var now = DateTime.Now;
            var targetTime = new DateTime(now.Year, now.Month, now.Day, 0, 0, 0);

            if (now >= targetTime)
            {
                // Check if next day has arrived
                targetTime = targetTime.AddDays(1);
            }

            var waitTime = targetTime - now;
            Console.WriteLine($"Next run scheduled for: {targetTime.ToString("yyyy-MM-dd HH:mm:ss")}");
            Console.WriteLine($"Waiting for: {waitTime.TotalMilliseconds} milliseconds");
            await page.WaitForTimeoutAsync(waitTime.TotalMilliseconds);

            // Trigger the DAG run
            await page.ClickAsync("#trigger_dag");
            await page.SelectOptionAsync("#dag_id", "capture_ezb.py"); // Assuming DAG ID is selected by dropdown
            await page.ClickAsync("button.confirm");
            await page.WaitForSelectorAsync(".alert-success"); // Wait for confirmation message

            Console.WriteLine($"DAG 'capture_ezb.py' triggered successfully!");
        }
    }
}
