import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  private products: Array<Product>;

  constructor() { }

  // 这个方法声明生命周期
  // ngOnInit属于Angular生命周期的一部分，其在第一轮ngOnChanges完成之后调用，并且只调用一次：
  ngOnInit() {

    this.products = [
      new Product(1,"第一个商品",1.99,3.5,"这是一个描述",["类别1","类别2"]),
      new Product(2,"第二个商品",1.99,4.5,"这是一个描述",["类别1","类别2"]),
      new Product(3,"第三个商品",15.99,1.5,"这是一个描述",["类别1","类别2"]),
      new Product(4,"第四个商品",13.99,5,"这是一个描述",["类别1","类别2"]),
      new Product(5,"第五个商品",11.99,3.5,"这是一个描述",["类别1","类别2"]),
      new Product(6,"第六个商品",12.99,3.5,"这是一个描述",["类别1","类别2"])
    ]
}
}

// 构造一个类，描述了包含的产品信息
export class Product {
  constructor(
    public id:number,
    public title:string,
    public price,
    public rating:number,
    public desc:string,
    public categories:Array<string>
  ){
    
  }
}