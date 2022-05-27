// Addinf event listners  when page is loaded
var lists={
    'web': {
        'frontend': ['React', 'Vue', 'Angular'],
        'backend': ['Django','Flask','SpringBoot','Node']
    },
    'mobile': {
        'frontend': ['React Native'],
        'backend': ['Django','FireBase','SpringBoot']
    }
    ,
    'desktop': {
        'frontend': ['Electron'],
        'backend': ['Django','Flask','SpringBoot']
    }
}
document.addEventListener('DOMContentLoaded', function() {
    listUpdate('web');
    // Use buttons to toggle between views
    document.querySelector('#web').addEventListener('click', () => listUpdate('web'));
    document.querySelector('#mobile').addEventListener('click', () => listUpdate('mobile'));
    document.querySelector('#desktop').addEventListener('click', () => listUpdate('desktop'));
    // document.querySelector('#compose-form').addEventListener('submit',SubmitEvent);
  });

  function listUpdate(name)
  {
      var flist= document.querySelector('#front-list');
      var blist= document.querySelector('#backend-list');
      flist.innerHTML='';
      blist.innerHTML='';
      var fopt='';
      var bopt='';
      lists[name].frontend.forEach(element => {
          fopt+= get_element(element,'frontend_opt');
      });
      lists[name].backend.forEach(element => {
        bopt+= get_element(element,'backend_opt');
    });
    flist.innerHTML=fopt;
    blist.innerHTML=bopt;
      

  }
  function get_element(val,opt)
  {
    const newEl = `
    <div class="form-check">
        <input class="form-check-input" type="radio" name="${opt}" id="${val}" value="${val}" checked>
        <label class="form-check-label" for="${val}">
        ${val}
        </label>
      </div>`;
      return newEl;
  }