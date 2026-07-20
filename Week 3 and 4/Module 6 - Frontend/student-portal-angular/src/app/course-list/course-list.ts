import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseCardComponent } from '../course-card/course-card';

import { CourseService } from '../services/course';

@Component({

  selector: 'app-course-list',

  standalone: true,

  imports: [

    CommonModule,

    FormsModule,

    CourseCardComponent

  ],

  templateUrl: './course-list.html',

  styleUrls: ['./course-list.css']

})

export class CourseListComponent {

  loading = true;

  courses: any[] = [];

  searchTerm = '';

  constructor(

private courseService: CourseService

){

this.courseService

.getCourses()

.subscribe(data=>{

this.courses=data;

this.loading=false;

});

}

 get filteredCourses() {

  return this.courses.filter(course =>

    course.title
      .toLowerCase()
      .includes(
        this.searchTerm.toLowerCase()
      )

  );

}

}