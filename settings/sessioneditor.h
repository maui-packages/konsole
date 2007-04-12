/***************************************************************************
                          sessioneditor.h  -  description
                             -------------------
    begin                : oct 28 2001
    copyright            : (C) 2001 by Stephan Binner
    email                : binner@kde.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#ifndef SESSIONEDITOR_H
#define SESSIONEDITOR_H

#include <Qt3Support/Q3PtrList>
#include <QStringList>
#include <QWidget>

#include "ui_sessiondialog.h"

class SessionDialog : public QWidget, public Ui::SessionDialog
{
public:
  SessionDialog( QWidget *parent ) : QWidget( parent ) {
    setupUi( this );
  }
};

class SessionEditor : public SessionDialog
{
  Q_OBJECT 
  public:
    SessionEditor(QWidget* parent=0);
    ~SessionEditor();
 
    bool isModified() const { return sesMod; }
    void querySave();

  Q_SIGNALS:
    void changed();
    void getList();

  public Q_SLOTS:
    void schemaListChanged(const QStringList &titles, const QStringList &filenames);

  private Q_SLOTS:
    void readSession(int);
    void saveCurrent();
    void removeCurrent();
    void sessionModified();

  private: 
    void load();
    void loadAllKeytab();
    void loadAllSession(QString currentFile="");
    QString readKeymapTitle(const QString& filename);

    bool sesMod;
    int oldSession;
    bool loaded;
    Q3PtrList<QString> keytabFilename;
    Q3PtrList<QString> schemaFilename;
};

#endif
