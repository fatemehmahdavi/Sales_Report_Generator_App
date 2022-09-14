const reportBtn=document.getElementById('report-btn')
const img=document.getElementById('img')

// https://www.freecodecamp.org/news/javascript-addeventlistener-example-code/
const modalBody=document.getElementById('modal-body')
const reportForm=document.getElementById('report-form')

const reportName=document.getElementById('id_name')
const reportRemarks=document.getElementById('id_remarks')
const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value

reportBtn.addEventListener('click',()=>{
    img.setAttribute('class','w-100')      // bootstrap class, 100% width of modalBody
    modalBody.prepend(img) //prepend adds the image to the top of the modal
    reportForm.addEventListener('submit',e=>{
        e.preventDefault() //we don't want to submit the form we or refresh.we want to continue working on the data we're going to send through an ajax call
        // The preventDefault() method cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur. For example, this can be useful when: Clicking on a "Submit" button, prevent it from submitting a form. Clicking on a link, prevent the link from following the URL.
        const formData=new formData()
        formData.append('csrfmiddlewaretoken',csrf)
        formData.append('name',reportName.value)
        formData.append('remarks',reportRemarks.value)
        formData.append('image',img.src)
        
    })
})