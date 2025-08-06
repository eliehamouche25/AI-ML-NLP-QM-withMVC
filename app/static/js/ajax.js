 
<script>
document.getElementById("fetchDataBtn").addEventListener("click", () => {
    fetch("/quantum/data")
        .then(response => response.json())
        .then(data => {
            const output = document.getElementById("zone4");
            output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        });
});
</script>


