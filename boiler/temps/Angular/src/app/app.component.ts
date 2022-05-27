import { Component, OnInit } from '@angular/core';
import { AppServiceService } from './app-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'clientssss';
  msg = 'Check';

  constructor(private service: AppServiceService) {}
  ngOnInit() {}

  clicked() {
    this.service.getData().subscribe(
      (response) => {
        this.msg = response;
        console.log('response from api is ', response);
      },
      (error) => {
        console.log('ERROR is ', error);
      }
    );
  }
}
