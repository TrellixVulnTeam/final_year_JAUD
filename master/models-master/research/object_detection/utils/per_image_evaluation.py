<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.18.3 -->
<interface>
  <requires lib="gtk+" version="3.0"/>
  <requires lib="LibreOffice" version="1.0"/>
  <object class="GtkDialog" id="SelectCertificateDialog">
    <property name="can_focus">False</property>
    <property name="border_width">6</property>
    <property name="title" translatable="yes">Select Certificate</property>
    <property name="resizable">False</property>
    <property name="type_hint">dialog</property>
    <child internal-child="vbox">
      <object class="GtkBox" id="dialog-vbox1">
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <property name="spacing">12</property>
        <child internal-child="action_area">
          <object class="GtkButtonBox" id="dialog-action_area1">
            <property name="can_focus">False</property>
            <property name="layout_style">end</property>
            <child>
              <object class="GtkButton" id="ok">
                <property name="label">gtk-ok</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="can_default">True</property>
                <property name="has_default">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="cancel">
                <property name="label">gtk-cancel</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="help">
                <property name="label">gtk-help</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">2</property>
                <property name="secondary">True</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="pack_type">end</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkGrid" id="grid1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="hexpand">True</property>
            <property name="vexpand">True</property>
            <property name="row_spacing">12</property>
            <property name="column_spacing">12</property>
            <child>
              <object class="GtkGrid" id="grid2">
                <property name="can_focus">False</property>
                <property name="no_show_all">True</property>
                <property name="hexpand">True</property>
                <property name="column_spacing">12</property>
                <child>
                  <object class="GtkLabel" id="issuedto">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Issued to  </property>
                  </object>
                  <packing>
                    <property name="left_attach">0</property>
                    <property name="top_attach">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="issuedby">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Issued by</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="top_attach">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="usage">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Certificate usage</property>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="top_attach">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="expiration">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Expiration date</property>
                  </object>
                  <packing>
                    <property name="left_attach">3</property>
                    <property name="top_attach">0</property>
                  </packing>
                </child>
                <!-- Just for localisation -->
                <child>
                  <object class="GtkLabel" id="STR_DIGITAL_SIGNATURE">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Digital signature</property>
                  </object>
                  <object class="GtkLabel" id="STR_NON_REPUDIATION">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Non-repudiation</property>
                  </object>
                  <object class="GtkLabel" id="STR_KEY_ENCIPHERMENT">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Key encipherment</property>
                  </object>
                  <object class="GtkLabel" id="STR_DATA_ENCIPHERMENT">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Data encipherment</property>
                  </object>
                  <object class="GtkLabel" id="STR_KEY_AGREEMENT">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Key Agreement</property>
                  </object>
                  <object class="GtkLabel" id="STR_KEY_CERT_SIGN">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Certificate signature verification</property>
                  </object>
                  <object class="GtkLabel" id="STR_CRL_SIGN">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">CRL signature verification</property>
                  </object>
                  <object class="GtkLabel" id="STR_ENCIPHER_ONLY">
                    <property name="can_focus">False</property>
                    <property name="hexpand">True</property>
                    <property name="label" translatable="yes">Only for encipherment</property>
                  </object>
                </child>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="label1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="xalign">0</property>
                <property name="ypad">1</property>
                <property name="label" translatable="yes">Select the certificate you want to use for signing:</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">0</property>
              </packing>
            </child>
            <child>
              <object class="svtlo-SvSimpleTableContainer" id="signatures">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="hexpand">True</property>
                <property name="vexpand">True</property>
                <child internal-child="selection">
                  <object class="GtkTreeSelection" id="Simple Table Container-selection1"/>
                </child>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="viewcert">
                <property name="label" translatable="yes">View Certificate...</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="halign">end</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkBox" id="dialog-hbox1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="spacing">12</property>
                <child>
                  <object class="GtkLabel" id="label2">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label" translatable="yes">Description:</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="description">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">4</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">True</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
    <action-widgets>
      <action-widget response="0">ok</action-widget>
      <action-widget response="0">cancel</action-widget>
      <action-widget response="0">help</action-widget>
    </action-widgets>
  </object>
</interface>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            