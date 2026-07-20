import { Component } from '@angular/core';

import {

  FormControl,

  FormGroup,

  ReactiveFormsModule,

  Validators

} from '@angular/forms';

import { CommonModule } from '@angular/common';

@Component({

  selector: 'app-student-profile',

  standalone: true,

  imports: [

    CommonModule,

    ReactiveFormsModule

  ],

  templateUrl: './student-profile.html',

  styleUrl: './student-profile.css'

})

export class StudentProfileComponent {

  profileForm = new FormGroup({

    name: new FormControl('', [

      Validators.required

    ]),

    email: new FormControl('', [

      Validators.required,

      Validators.email

    ]),

    semester: new FormControl('', [

      Validators.required,

      Validators.min(1),

      Validators.max(8)

    ])

  });

 onSubmit() {

  console.log("Submitted!");

  console.log(this.profileForm.value);

  alert("Profile Submitted Successfully");

}

}