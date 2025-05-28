    // const url = ""
    document.querySelector("#btn").addEventListener("click", ()=> {
        let query =  document.getElementById("url").value;
        console.log(query)
       
     fetch(`http://127.0.0.1:5001/submit?query=${query}`)
     
     .then(
         response =>response.json()
     )
     
     .then(
         res =>{
         // console.log(res["result"])
         document.querySelector("#summary-text").textContent = res["result"]
        })
     
     })

     let copySummary = () => {
        // Get the text content
        let summaryText = document.getElementById('summary-text');

        if(summaryText.textContent == ""){
            // alert("I need something to copy");
            console.log("test");
            summaryText.innerText= "";
        }
        else{
            // Copy to clipboard
            navigator.clipboard.writeText(summaryText.textContent).then(() => {
            // Show feedback
            const button = document.getElementById('copy-button');
            button.textContent = 'Copied!';
            setTimeout(() => {
              button.textContent = 'Copy';
            }, 2000);
          }).catch(err => {
            console.error('Failed to copy text:', err);
          });
        }

    }