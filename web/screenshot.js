const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 1400 });

  await page.goto("http://localhost:8080/", { waitUntil: "networkidle0" });
  await page.screenshot({ path: "screenshot-home.png", fullPage: true });

  await page.goto("http://localhost:8080/chapter0/", { waitUntil: "networkidle0" });
  await page.screenshot({ path: "screenshot-chapter0.png", fullPage: true });

  await browser.close();
  console.log("Done");
})();
