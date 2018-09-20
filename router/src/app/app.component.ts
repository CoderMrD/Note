import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'router';

  // 这样可以拿到一个router对象，依赖注入中的内容
  constructor(private router:Router){
  }

  toProductDetails(){
    this.router.navigate(['/product',2])
  }
}
