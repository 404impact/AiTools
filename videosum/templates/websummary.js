    // const url = ""
    document.querySelector("#btn").addEventListener("click", ()=> {
        let query =  document.getElementById("content").value;
        console.log(query)
       
     fetch(`http://127.0.0.1:5100/submit?query=${query}`)
     
     .then(
         response =>response.json()
     )
     
     .then(
         res =>{
         // console.log(res["result"])
         document.querySelector("#output_container").textContent = res["result"]
     })
     
     })