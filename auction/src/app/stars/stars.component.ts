import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-stars',
  templateUrl: './stars.component.html',
  styleUrls: ['./stars.component.css']
})
export class StarsComponent implements OnInit {

  // 表示这个星级评价的组件属性应该又他的父组件传递进来
  @Input()
  private rating:number = 0;
  private stars: boolean[];

  constructor() { }

  ngOnInit() {
    this.stars = [];
    // 根据星级来判断true和false
    for (let i=1; i<=5; i++){
      this.stars.push(i > this.rating)
    }
  }

}
// export class 
