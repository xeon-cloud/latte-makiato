def getUi():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>0</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Название сорта</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="l1">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>10</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="l2">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>80</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="l3">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>150</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>80</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Степень обжарки</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>150</y>
      <width>181</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Молотый / в зернах</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>230</y>
      <width>191</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Описание вкуса</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>310</y>
      <width>201</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Цена</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>400</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Объём упаковки</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="l4">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>230</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="l5">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>320</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="l6">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>400</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>470</y>
      <width>261</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(242, 255, 94);</string>
    </property>
    <property name="text">
     <string>Добавить запись</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''