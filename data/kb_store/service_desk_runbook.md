# IT Service Desk Troubleshooting Runbook

**Document Type:** IT Operations and Troubleshooting Guide  
**Document ID:** IT-RB-001  
**Version:** 1.0  
**Status:** Demo / Dummy Knowledge Base  
**Department:** IT Service Desk  
**Last Updated:** October 2026

> **Note:** This is fictional sample content intended for retrieval, question answering, and troubleshooting demonstrations. The procedures must be adapted to the actual IT environment before production use.

## 1. Purpose

This runbook provides repeatable troubleshooting procedures for common IT support incidents.

The IT Support Agent should use these procedures to identify likely causes, recommend safe diagnostic steps, and determine when human support or security escalation is required.

The agent must not claim that a problem has been fixed unless the user confirms the result or a connected system verifies the outcome.

## 2. General Troubleshooting Workflow

For every IT issue, follow this workflow:

1. Identify the affected device, application, or service.
2. Ask for the exact error message if the issue is unclear.
3. Determine when the problem started and whether other users are affected.
4. Check the simplest and safest likely causes first.
5. Recommend one or more relevant troubleshooting steps.
6. Ask the user to test the affected function again.
7. If the issue persists, collect diagnostic information and escalate.
8. Record the symptoms, steps attempted, and results in the support ticket.

Do not ask users to disclose passwords, MFA codes, private keys, or other authentication secrets.

## 3. Incident Priority Guidelines

| Priority      | Description                                           | Example                                           |
| ------------- | ----------------------------------------------------- | ------------------------------------------------- |
| P1 — Critical | Major service disruption or serious security incident | Organization-wide outage or suspected ransomware  |
| P2 — High     | Important business function unavailable               | Employee cannot access a critical business system |
| P3 — Medium   | Individual user affected with a workaround available  | Email client malfunction with webmail available   |
| P4 — Low      | Minor issue or routine request                        | Approved software installation request            |

These priority definitions are demonstration guidelines. Actual priorities and response targets must follow the organization's approved service-level agreements.

Security incidents should be escalated according to the organization's incident-response process, even if their immediate operational impact appears small.

## 4. Troubleshooting: Forgotten Password

**Incident ID:** INC-001  
**Category:** Account and Access

### Symptoms

- The user cannot sign in.
- The system reports an incorrect password.
- The user has forgotten their password.

### Possible Causes

- Incorrect password entry.
- Incorrect username or account domain.
- Keyboard layout or Caps Lock issue.
- Expired credentials.
- Account lockout.
- Identity-provider or authentication service problem.

### Resolution Steps

1. Confirm that the user is accessing the correct official sign-in page.
2. Verify the username and organization domain.
3. Check Caps Lock and keyboard layout.
4. Use the approved password-reset procedure.
5. Complete the required identity verification.
6. Retry sign-in with the newly established credentials.
7. If access still fails, check for an account lockout or identity-service issue through authorized support tools.
8. Escalate to the identity-management administrator when necessary.

### Escalation Criteria

Escalate when self-service recovery fails, the account remains locked, or there are indications of unauthorized access.

### Verification

Ask the user to sign in successfully and confirm that the required application is accessible.

## 5. Troubleshooting: Laptop Running Slowly

**Incident ID:** INC-002  
**Category:** Hardware and Performance

### Symptoms

- Applications open slowly.
- The system freezes or becomes unresponsive.
- The fan runs continuously.
- Boot time is unusually long.

### Possible Causes

- Too many applications running simultaneously.
- Insufficient available memory.
- Low disk space.
- Pending operating-system updates.
- High CPU or disk utilization.
- An application consuming excessive resources.
- Possible malware or hardware problems.

### Resolution Steps

1. Ask whether the problem started recently or has been present for a long time.
2. Save open work.
3. Restart the computer if it is safe to do so.
4. Open the operating system's task-management utility.
5. Identify applications consuming unusually high CPU, memory, or disk resources.
6. Close unnecessary applications, ensuring that important work is saved.
7. Check available disk space and use approved cleanup procedures if needed.
8. Check for pending operating-system updates.
9. Run the organization's approved endpoint-security scan if suspicious activity is suspected.
10. If performance remains poor, collect device specifications, resource-usage information, and relevant error messages for IT Support.

### Safety Notes

Do not instruct users to disable security software, delete unfamiliar system files, or terminate critical system processes.

### Escalation Criteria

Escalate if the computer repeatedly freezes, overheats, displays hardware errors, or remains slow after basic troubleshooting.

## 6. Troubleshooting: Wi-Fi Not Connecting

**Incident ID:** INC-003  
**Category:** Network

### Symptoms

- The laptop cannot connect to Wi-Fi.
- The network is visible but the connection fails.
- The device reports limited connectivity.
- The user cannot access the internet.

### Possible Causes

- Wi-Fi is disabled.
- Airplane mode is enabled.
- Incorrect network selection.
- Authentication failure.
- Router or access-point problem.
- DHCP or DNS configuration issue.
- Network outage.

### Resolution Steps

1. Verify that Wi-Fi is enabled.
2. Confirm that airplane mode is disabled.
3. Check that the correct corporate network is selected.
4. Disconnect and reconnect to the approved network.
5. Determine whether other devices are affected.
6. Test access to an approved internal resource and an external website, if permitted.
7. Restart the device if appropriate.
8. If the problem continues, report the error message and whether other users are affected.
9. IT Support should inspect network availability, authentication, DHCP, DNS, and access-point status using authorized tools.

### Escalation Criteria

Escalate if multiple employees are affected, the corporate network is unavailable, or authentication repeatedly fails.

### Verification

Confirm that the user can connect and access the required business resources.

## 7. Troubleshooting: VPN Not Connecting

**Incident ID:** INC-004  
**Category:** Remote Access

### Symptoms

- The VPN client cannot establish a connection.
- The VPN connection times out.
- Authentication fails.
- The VPN connects but internal applications remain inaccessible.

### Possible Causes

- No internet connection.
- Incorrect VPN gateway configuration.
- Authentication or MFA failure.
- Expired or revoked access.
- VPN service outage.
- Firewall or network restrictions.
- DNS or routing problem.

### Resolution Steps

1. Verify that the device can access the internet without the VPN, where appropriate.
2. Confirm that the organization-approved VPN client is being used.
3. Verify the configured VPN gateway against official IT instructions.
4. Check the displayed error message.
5. Retry authentication once after confirming the username and approved MFA method.
6. Check the official service-status channel for a known outage.
7. Restart the VPN client and retry.
8. If the VPN connects but internal services remain unavailable, report the affected application and error.
9. IT Support should verify user permissions, gateway health, authentication logs, and network routes.

### Security Notes

Do not bypass VPN security checks, install unauthorized VPN clients, or share authentication codes.

### Escalation Criteria

Escalate if the user cannot establish a connection after basic checks, access is unexpectedly revoked, or multiple users report the same failure.

## 8. Troubleshooting: Email Not Working

**Incident ID:** INC-005  
**Category:** Email and Collaboration

### Symptoms

- Email messages are not arriving.
- Messages remain in the Outbox.
- The email application cannot synchronize.
- The mailbox reports an error.
- Attachments cannot be sent.

### Possible Causes

- Network connectivity problem.
- Incorrect account configuration.
- Expired authentication session.
- Mailbox storage limit reached.
- Attachment size or file-type restriction.
- Mail service outage.
- Message filtering or delivery issue.

### Resolution Steps

1. Verify that the internet connection works.
2. Confirm that the correct work account is selected.
3. Refresh the mailbox or restart the email client.
4. Sign in to the approved webmail interface, if available.
5. Check whether the issue affects sending, receiving, or both.
6. Check mailbox capacity and attachment restrictions.
7. Review any non-sensitive error message displayed by the application.
8. Check the approved service-status channel for a mail outage.
9. If the issue persists, IT Support should inspect account status, mail flow, and relevant service logs.

### Escalation Criteria

Escalate when email remains unavailable, multiple users are affected, or important business messages are delayed.

### Verification

Send a permitted test message and confirm that it is delivered successfully.

## 9. Troubleshooting: Software Installation Failure

**Incident ID:** INC-006  
**Category:** Software

### Symptoms

- An installer fails.
- The system reports insufficient permissions.
- The installation stops unexpectedly.
- An application does not launch after installation.

### Possible Causes

- Insufficient disk space.
- Unsupported operating-system version.
- Missing dependencies.
- Installer corruption.
- Administrator permissions required.
- Software blocked by organizational policy.
- Endpoint-security restriction.

### Resolution Steps

1. Confirm the application name and approved source.
2. Check whether the application is authorized by the organization.
3. Review the exact installation error.
4. Check available disk space.
5. Verify operating-system compatibility.
6. Retry using the official installer or company software portal.
7. If administrator rights are required, submit an IT support request.
8. Provide the installer name, version, error message, and installation time to IT Support.

### Security Notes

Never bypass administrator restrictions or disable endpoint protection to force an installation.

### Escalation Criteria

Escalate when an approved application cannot be installed or when an installation is blocked by a security policy.

## 10. Troubleshooting: Printer Not Printing

**Incident ID:** INC-007  
**Category:** Peripheral Devices

### Symptoms

- Print jobs remain queued.
- The printer is offline.
- Documents print with missing content.
- The printer does not respond.

### Possible Causes

- Printer is powered off.
- Paper or toner is unavailable.
- Incorrect printer selected.
- Network connectivity issue.
- Print queue or spooler problem.
- Driver or configuration issue.

### Resolution Steps

1. Verify that the printer is powered on.
2. Check the printer display for paper, toner, or hardware warnings.
3. Confirm that the correct printer is selected.
4. Check the device's printer queue.
5. Confirm network connectivity for network printers.
6. Retry with a simple test page if permitted.
7. Restart the printer only if appropriate and authorized.
8. Contact IT Support if jobs remain queued or driver errors occur.

### Escalation Criteria

Escalate when multiple users cannot print, the printer reports a hardware fault, or the queue remains blocked.

## 11. Troubleshooting: Application Crashes

**Incident ID:** INC-008  
**Category:** Application Support

### Symptoms

- The application closes unexpectedly.
- The application freezes.
- An error appears when opening a file.
- A specific operation causes repeated crashes.

### Possible Causes

- Software defect.
- Incompatible application version.
- Corrupted configuration.
- Insufficient system resources.
- Damaged input file.
- Missing dependency.
- Operating-system compatibility issue.

### Resolution Steps

1. Record the application name and version.
2. Capture the exact error message without including confidential data.
3. Determine whether the issue affects one file or all files.
4. Save work and restart the application.
5. Restart the computer if necessary.
6. Check for approved application updates.
7. Test with a non-sensitive sample file if appropriate.
8. Report the crash frequency, reproduction steps, and relevant timestamps to IT Support.

### Escalation Criteria

Escalate when the crash is reproducible, affects business-critical work, or causes data loss.

## 12. Troubleshooting: Suspected Phishing or Malware

**Incident ID:** SEC-001  
**Category:** Security Incident

### Symptoms

- A suspicious email requests credentials or payment.
- An unexpected attachment prompts the user to enable macros.
- A browser redirects to an unfamiliar login page.
- Endpoint protection displays a malware alert.
- Files suddenly become inaccessible or show unusual extensions.
- An account receives unexpected MFA prompts.

### Immediate Response

1. Stop interacting with the suspicious message, file, or website.
2. Do not enter credentials or approve unexpected authentication requests.
3. Report the incident through the organization's approved security channel.
4. Provide the approximate time, affected device, suspicious message details, and any observed symptoms.
5. Follow instructions from the security team regarding network isolation, account protection, or device handling.
6. If credentials were entered into a suspicious site, notify IT Security immediately and follow the approved credential-recovery process.

### Important Restrictions

- Do not delete evidence or suspicious files unless instructed by the security team.
- Do not attempt to investigate suspected malware using unauthorized tools.
- Do not forward suspicious attachments unless the approved reporting procedure specifically requires it.
- Do not claim that a device is clean solely because a scan reports no detections.

### Escalation Criteria

Treat suspected ransomware, unauthorized account access, confidential-data exposure, and active malware alerts as security incidents requiring prompt escalation.

## 13. Troubleshooting: Computer Will Not Start

**Incident ID:** INC-009  
**Category:** Hardware

### Symptoms

- The laptop does not power on.
- The screen remains blank.
- The device starts but does not load the operating system.
- The computer shuts down unexpectedly during startup.

### Possible Causes

- Battery discharged.
- Faulty charger or power connection.
- Display issue.
- Hardware failure.
- Operating-system boot problem.

### Resolution Steps

1. Check the power adapter and wall connection.
2. Verify that the charging indicator appears, if available.
3. Disconnect unnecessary external peripherals.
4. Attempt a normal power-on.
5. Observe any indicator lights, beeps, or error messages.
6. Avoid repeatedly forcing shutdowns if the device is in the middle of a system update.
7. Contact IT Support if the laptop remains unresponsive or displays hardware errors.

### Escalation Criteria

Escalate if there is a burning smell, visible damage, liquid exposure, unusual heat, or repeated failure to start. Disconnect power if safe to do so and do not continue using damaged equipment.

## 14. Troubleshooting: Insufficient Disk Space

**Incident ID:** INC-010  
**Category:** System Maintenance

### Symptoms

- The operating system reports low disk space.
- Applications cannot save files.
- Updates fail.
- The computer becomes slow.

### Resolution Steps

1. Check available storage through the operating system's storage settings.
2. Identify large files in user-controlled folders.
3. Move appropriate work files to approved storage locations.
4. Empty the recycle bin only after confirming that no required files remain.
5. Use the operating system's approved temporary-file cleanup feature.
6. Avoid deleting unfamiliar system folders or application data.
7. Contact IT Support if storage remains insufficient or cleanup requires administrator access.

### Escalation Criteria

Escalate if disk space continues to decrease unexpectedly, storage errors appear, or the drive may be failing.

## 15. Standard Ticket Information Template

When troubleshooting cannot resolve the problem, collect the following information:

- **Ticket ID:** Assigned by the support system.
- **Issue Category:** Account, Network, Email, Hardware, Software, or Security.
- **Affected Device/Application:** User-provided details.
- **Problem Description:** What is happening?
- **Error Message:** Exact non-sensitive text, if available.
- **Start Time:** When did the issue begin?
- **Scope:** One user, multiple users, or organization-wide.
- **Business Impact:** What work is blocked?
- **Troubleshooting Attempted:** Steps and their results.
- **Priority:** Assigned according to the approved priority policy.
- **Escalation Required:** Yes or No.

Do not put passwords, authentication codes, private keys, or other secrets in support tickets.

## 16. Frequently Asked Troubleshooting Questions

**Q: My laptop is very slow. What should I do?**

A: Save your work, restart the computer if appropriate, check CPU and memory usage, close unnecessary applications, and check disk space. If the issue persists, contact IT Support with the observed symptoms.

**Q: My VPN says authentication failed. How do I fix it?**

A: Confirm the official VPN gateway and username, verify that your approved authentication method works, and check for a service outage. Do not share authentication codes. Escalate if access continues to fail.

**Q: I cannot receive emails. What should I check?**

A: Verify internet access, refresh the email client, test approved webmail, and check for mailbox or service issues. Contact IT Support if messages remain unavailable.

**Q: My software installation requires administrator access. Can I bypass it?**

A: No. Submit a software installation request and allow authorized IT personnel to complete the installation.

**Q: I received an unexpected MFA notification. What should I do?**

A: Do not approve it. Report it to IT Security immediately and follow the organization's account-protection instructions.

**Q: When should an IT problem be escalated?**

A: Escalate when basic troubleshooting fails, a critical business service is unavailable, multiple users are affected, data loss is possible, or a security incident is suspected.

**Q: What if the agent cannot find a solution in the knowledge base?**

A: The agent should acknowledge the limitation, ask for relevant non-sensitive diagnostic details, and recommend opening a support ticket. It must not invent company-specific procedures or claim an unverified fix.

## 17. Guidance for the AI Support Agent

When using this runbook to answer questions:

1. Retrieve the troubleshooting procedure that best matches the user's issue.
2. Present the most relevant steps in a clear and actionable order.
3. Ask a clarifying question if the issue is ambiguous.
4. Prefer safe, reversible checks before disruptive actions.
5. Do not request passwords, MFA codes, or confidential secrets.
6. Clearly distinguish documented facts from possible causes.
7. Escalate security incidents promptly.
8. Do not invent internal contact details, service availability, or resolution guarantees.
9. Ask the user to confirm whether the recommended steps resolved the problem.
10. If no matching procedure is available, say so and recommend the approved support process.
