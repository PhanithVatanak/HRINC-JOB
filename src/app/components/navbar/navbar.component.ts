import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  toggleMode : boolean = false

  constructor() {}

  ngOnInit(): void {}

  nightModeToggle(){
    if(this.toggleMode == false){
      this.toggleMode = true

      console.log('night mode is on')
    } else {
      this.toggleMode = false
      console.log('night mode is off')
    }
  }
}
