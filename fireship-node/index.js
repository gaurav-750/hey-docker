const app = require("express")();

app.get("/", (req, res) => {
  res.json({ message: "Hello there, from Node-Docker!" });
});

const port = process.env.PORT || 8000;

app.listen(port, () => {
  console.log(`App is listening on port: ${port}`);
});
