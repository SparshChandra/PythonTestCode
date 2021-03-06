<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="windowModality">
   <enum>Qt::NonModal</enum>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>552</width>
    <height>297</height>
   </rect>
  </property>
  <property name="mouseTracking">
   <bool>false</bool>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="1" column="2">
     <layout class="QGridLayout" name="gridLayout_2">
      <item row="4" column="0" colspan="3">
       <spacer name="verticalSpacer_3">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>0</width>
          <height>0</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="7" column="0" colspan="3">
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="QPushButton" name="register_2">
          <property name="text">
           <string>Register</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="login">
          <property name="text">
           <string>Login</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="guest">
          <property name="text">
           <string>Guest</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item row="5" column="0">
       <widget class="QLabel" name="label_2">
        <property name="text">
         <string>Password</string>
        </property>
       </widget>
      </item>
      <item row="5" column="1" colspan="2">
       <widget class="QLineEdit" name="passwd"/>
      </item>
      <item row="3" column="0">
       <widget class="QLabel" name="label">
        <property name="text">
         <string>Email</string>
        </property>
       </widget>
      </item>
      <item row="3" column="1" colspan="2">
       <widget class="QLineEdit" name="username"/>
      </item>
      <item row="6" column="0" colspan="3">
       <spacer name="verticalSpacer_4">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>0</width>
          <height>0</height>
         </size>
        </property>
       </spacer>
      </item>
     </layout>
    </item>
    <item row="1" column="3">
     <spacer name="horizontalSpacer">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>0</width>
        <height>0</height>
       </size>
      </property>
     </spacer>
    </item>
    <item row="1" column="1">
     <spacer name="horizontalSpacer_3">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>0</width>
        <height>0</height>
       </size>
      </property>
     </spacer>
    </item>
    <item row="2" column="2">
     <spacer name="verticalSpacer">
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>0</width>
        <height>0</height>
       </size>
      </property>
     </spacer>
    </item>
    <item row="1" column="0">
     <spacer name="horizontalSpacer_2">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>0</width>
        <height>0</height>
       </size>
      </property>
     </spacer>
    </item>
    <item row="0" column="2">
     <spacer name="verticalSpacer_2">
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>0</width>
        <height>0</height>
       </size>
      </property>
     </spacer>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>