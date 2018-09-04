function HandleEvents(data) {

  const socket = io();

  socket.emit('info', data)

  socket.on('info', (res) => {

    const alert = GetElement('alert')
    alert.innerHTML = res
    alert.classList.remove('hide')
    alert.classList.add('show')

    setTimeout(() => {
      alert.classList.remove('show')
      alert.classList.add('hide')
    },2000)

  })

}

function GetElement(id) {
  return document.getElementById(id)
}

const btn_send = GetElement('btn_send');
const name = GetElement('name');

btn_send.addEventListener('click', () => {
  const myname = name.value;

  if (myname.trim() != "") {
    HandleEvents({ name: myname });
    name.value = "";
  }

})

