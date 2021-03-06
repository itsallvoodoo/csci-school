/*
 * OpenRemote, the Home of the Digital Home.
 * Copyright 2008-2010, OpenRemote Inc.
 *
 * See the contributors.txt file in the distribution for a
 * full listing of individual contributors.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
package org.openremote.controller;


/**
 * This class provides the Java bindings from config.properties file found in
 * <tt>WEB-INF/classes</tt> directory of the web archive.
 *
 * <p>
 * The actual value injection is currently configured via Spring frameworks'
 * <tt>applicationContext.xml</tt> configuration file also found in the web archive.
 * Each additional configuration property must be added to the XML definition
 * as well as a Java accessor method implementation in this class.
 *
 * @author Dan Cong
 * @author <a href="mailto:juha@openremote.org>Juha Lindfors</a>
 * @author Jerome Velociter
 */
public class Configuration extends CustomConfiguration {

  // Constants ------------------------------------------------------------------------------------

  /* the following constants are the keys from config.properties */

  public static final String RESOURCE_UPLOAD_ENABLE = "resource.upload.enable";
  public static final String RESOURCE_PATH = "resource.path";
  public static final String IRSEND_PATH = "irsend.path";
  public static final String MULTICAST_PORT = "multicast.port";
  public static final String MULTICAST_ADDRESS = "multicast.address";
  public static final String WEBAPP_PORT = "webapp.port";
  public static final String COPY_LIRCD_CONF_ON = "copy.lircd.conf.on";
  public static final String LIRCD_CONF_PATH = "lircd.conf.path";
  public static final String WEBAPP_IP = "webapp.ip";
  public static final String BEEHIVE_REST_ROOT_URL = "beehive.REST.Root.Url";
  public static final String CONTROLLER_APPLICATIONNAME = "controller.applicationname";

  // Class Methods --------------------------------------------------------------------------------

  public static Configuration parseFromControllerXML() {

     return null;
  }

  
  // Private Instance Variables -------------------------------------------------------------------
  
   /** The irsend path. */
   private String irsendPath;
   
   /** The lircd.conf path. */
   private String lircdconfPath;
   
   /** Whether copy lircd.conf for user. */
   private boolean copyLircdconf;
   
   /** The webapp port. */
   private int webappPort;
   
   /** The multicast address. */
   private String multicastAddress;
   
   /** The multicast port. */
   private int multicastPort;
   
   /** The resource path. */
   private String resourcePath;
   
   /** The resource upload switch. */
   private boolean resourceUpload;
   
   private long macroIRExecutionDelay = 500;
   
   private String webappIp;
   
   private String beehiveRESTRootUrl;

   private String webappName;

  /**
   * The COM (Serial) port the ORC should use (for example, to send X10 events)
   */
  private String comPort;

  /**
   * The transmitter to use for X10
   */
  private String x10transmitter;


  // Public Methods -------------------------------------------------------------------------------

  /**
   * Returns a string containing an operating system specific filesystem path to
   * a executable LIRC 'irsend' command.
   *
   * @see #setIrsendPath(String)
   *
   * @return operating system specific filesystem path
   */
  public String getIrsendPath() {
    return preferAttrCustomValue(IRSEND_PATH, irsendPath);
  }

  /**
   * An operating system specific filesystem path as a string to a LIRC 'irsend'
   * executable command.
   *
   * @see #getIrsendPath()
   *
   * @param irsendPath operating system specific filesystem path
   */
  public void setIrsendPath(String irsendPath) {
    // TODO :
    //  could attempt to convert the string to a valid URI to support
    //  a system neutral path format ?
    //
    // TODO :
    //  should be explicit about (how-to) the use of relative paths

    this.irsendPath = irsendPath.trim();
  }

  /**
   * Returns a string containing an operating system specific filesystem path to
   * LIRC daemon configuration file.
   *
   * @see #setLircdconfPath(String)
   *
   * @return operating system specific filesystem path
   */
  public String getLircdconfPath() {
    return preferAttrCustomValue(LIRCD_CONF_PATH, lircdconfPath);
  }

  /**
   * An operating system specific filesystem path as a string to a LIRC 'lircd.conf' file
   * (containing all the infrared remote codes).
   *
   * @see #getLircdconfPath()
   *
   * @param lircdconfPath operating system specific path
   */
  public void setLircdconfPath(String lircdconfPath) {
    // TODO :
    //  could attempt to convert the string to a valid URI to support
    //  a system neutral path format ?
    //
    // TODO :
    //  should be explicit about (how-to) the use of relative paths

    this.lircdconfPath = lircdconfPath.trim();
  }

  /**
   * Indicates whether an existing 'lircd.conf' file is overriden on the system
   * when a new controller configuration is deployed through the web interface.
   *
   * @see #setCopyLircdconf(boolean)
   *
   * @return true if copy-over on configuration deployment is enabled; false otherwise
   */
  public boolean isCopyLircdconf() {
    return preferAttrCustomValue(COPY_LIRCD_CONF_ON, copyLircdconf);
  }

  /**
   * Determines whether a 'lircd.conf' file in a deployed controller configuration should
   * be copied over an existing LIRC configuration file found in the path returned by
   * {@link #getLircdconfPath()} method.  <p>
   *
   * <b>Important Note:</b> This is potentially disruptive to the user's system if an existing,
   * unrelated LIRC daemon configuration was already in use.
   *
   * @see #isCopyLircdconf()
   *
   * @param copyLircdconf  If true, enables copy-over behavior. If false, requires manual
   *                       infrared configuration in 'lircd.conf' file.
   */
  public void setCopyLircdconf(boolean copyLircdconf) {
    this.copyLircdconf = copyLircdconf;
  }

  /**
   * Returns the port number used by controller discovery service.
   *
   * @see #setWebappPort(int)
   *
   * @return port number
   */
  public int getWebappPort() {
    return preferAttrCustomValue(WEBAPP_PORT, webappPort);
  }

  /**
   * The port number the controller returns on a panel discovery request. It should
   * match the port number configured on the hosting web container or otherwise
   * things just don't work right.  <p>
   *
   * TODO:
   *   This is a duplicate configuration and should be consolidated with a proper service
   *   container around the web container. It should only be necessary to define the
   *   port number once.
   *
   * @see #getWebappPort()
   *
   * @param webappPort  the HTTP listening port of the web container (e.g. Tomcat 8080)
   */
  public void setWebappPort(int webappPort) {
    this.webappPort = webappPort;
  }

  /**
   * Returns the configured controller discovery multicast address
   *
   * @see #setMulticastAddress(String)
   *
   * @return IP multicast address as a string
   */
  public String getMulticastAddress() {
    return preferAttrCustomValue(MULTICAST_ADDRESS, multicastAddress);
  }

  /**
   * Sets the multicast address used for controller discovery by panels.
   *
   * @see #getMulticastAddress()
   *
   * @param multicastAddress IP multicast address as a string
   */
  public void setMulticastAddress(String multicastAddress) {

    // TODO : actually validate a correctly configured IP address

    this.multicastAddress = multicastAddress.trim();
  }

  /**
   * Returns the configured multicast port used for controller discovery.
   *
   * @return  multicast port
   */
  public int getMulticastPort() {
    return preferAttrCustomValue(MULTICAST_PORT, multicastPort);
  }

  /**
   * Sets the multicast port used for controller discovery.
   *
   * @see #getMulticastPort()
   *
   * @param multicastPort port number
   */
  public void setMulticastPort(int multicastPort) {
    this.multicastPort = multicastPort;
  }

  /**
   * Returns an operating system specific string containing a filesystem path
   * to a directory with the resource files of a controller
   *
   * @see #setResourcePath(String)
   *
   * @return operating system specific filesystem path as a string
   */
  public String getResourcePath() {
//      return preferAttrCustomValue(RESOURCE_PATH, resourcePath);
     return resourcePath;
  }

  /**
   * The resource path points to a directory where the controller looks for all
   * configuration files, images and other resources for panels and controllers.
   *
   * @see #getResourcePath()
   *
   * @param resourcePath  system specific filesystem path as a string to a directory containing
   *                      the resource files of a controller
   */
  public void setResourcePath(String resourcePath) {

    // TODO :
    //  could attempt to convert the string to a valid URI to support
    //  a system neutral path format ?
    //
    // TODO :
    //  should be explicit about (how-to) the use of relative paths

    this.resourcePath = resourcePath.trim();
  }

  /**
   * Indicates if controller mapping configuration deployment has been
   * enabled on the web user interface.
   *
   * @see #setResourceUpload(boolean)
   *
   * @return true if controller configuration can be uploaded through
   *         web interface; false otherwise
   */
  public boolean isResourceUpload() {
    return preferAttrCustomValue(RESOURCE_UPLOAD_ENABLE, resourceUpload);
  }

  /**
   * Enables the ability to upload controller event and command mappings
   * directly from the web user interface.  <p>
   *
   * This is a convenience feature for home users for easy deployment of
   * the controller configuration in cases where all users of the network
   * are trusted, or the controller is still being configured and tested. <p>
   *
   * As a security consideration, when deploying the controller on a public
   * network, this setting should always be disabled. <p>
   *
   * When disabled, configuration must be handled manually by copying all
   * the controller configuration files manually to a directory pointed by
   * {@link #setResourcePath} property. Access to this directory in the
   * filesystem should be properly secured with access restrictions. <p>
   *
   * @param resourceUpload  true to enable controller mapping uploads via
   *                        web interface; false otherwise
   *
   * @see #setResourcePath
   * @see #isResourceUpload
   */
  public void setResourceUpload(boolean resourceUpload) {
    this.resourceUpload = resourceUpload;
  }


  /**
   * Returns the name of the serial port configured for X10 serial PLM unit
   *
   * @see #setComPort(String)
   *
   * @return the name of the COM (serial) port or device
   */
  public String getComPort() {
    return comPort;
  }

  /**
   * Serial port or device to use with X10 serial power-line modules
   * (e.g. CM11A or CM17A "FireCracker" modules).
   *
   * Serial port configuration is specific to the operating system in use.
   * On Linux '/dev/ttyS0' or similar device name should be used. For
   * Microsoft Windows systems use port names such as COM1, COM2, etc.
   *
   * @see #getComPort()
   *
   * @param comPort the name of the COM (serial) port or device
   */
  public void setComPort(String comPort) {
    this.comPort = comPort.trim();
  }

  /**
   * TODO
   *
   * @see #setX10transmitter(String)
   *
   * @return
   */
  public String getX10transmitter() {
    return x10transmitter;
  }

  /**
   * TODO
   *
   * @see #getX10transmitter()
   *
   * @param x10transmitter
   */
  public void setX10transmitter(String x10transmitter) {
    this.x10transmitter = x10transmitter.trim();
  }

   public long getMacroIRExecutionDelay() {
      return preferAttrCustomValue("Macro.IR.Execution.Delay", macroIRExecutionDelay);
   }

   public void setMacroIRExecutionDelay(long macroIRExecutionDelay) {
      this.macroIRExecutionDelay = macroIRExecutionDelay;
   }

   public String getWebappIp() {      
      return preferAttrCustomValue(WEBAPP_IP, webappIp);
   }

   public void setWebappIp(String webappIp) {
      this.webappIp = webappIp;
   }

   public String getBeehiveRESTRootUrl() {
      return preferAttrCustomValue(BEEHIVE_REST_ROOT_URL, beehiveRESTRootUrl);
   }

   public void setBeehiveRESTRootUrl(String beehiveRESTRootUrl) {
      this.beehiveRESTRootUrl = beehiveRESTRootUrl;
   }
   
   public String getWebappName() {
      return preferAttrCustomValue(CONTROLLER_APPLICATIONNAME, webappName);
   }
   
   public void setWebappName(String webappName) {
      this.webappName = webappName;
   }
   
}
