# Threat Model Report

**Generated:** 2026-02-05 09:21 UTC  
**Repository:** https://github.com/asa1997/health_record_demo  
**Branch:** main  
**Language:**   
**Framework:** unknown  
**Architecture:** Unknown  
**Tool:** TITO (Threat In, Threat Out)  

---

## Executive Summary

TITO identified **7 threats** across **18 assets** with **69 data flows**.

| Severity | Count |
|----------|-------|
| 🔴 Critical | 0 |
| 🟠 High | 3 |
| 🟡 Medium | 4 |
| 🟢 Low | 0 |

## 1. Assets

**Total:** 18 assets | **Exposed:** 9 | **Sensitive:** 5

| Type | Count | Exposed | Sensitive |
|------|-------|---------|----------|
| api | 9 | 9 | 1 |
| filesystem | 4 | 0 | 0 |
| cryptography | 2 | 0 | 2 |
| database | 2 | 0 | 2 |
| network | 1 | 0 | 0 |

### Exposed Assets

| Asset | Type | Location |
|-------|------|----------|
| unknown | api | `agent.py:19` |
| unknown | api | `agent.py:23` |
| unknown | api | `agent.py:81` |
| unknown | api | `agent.py:138` |
| unknown | api | `agent.py:140` |
| unknown | api | `agent.py:178` |
| unknown | api | `agent.py:190` |
| unknown | api | `agent.py:192` |
| /call_api | api | `agent.py:197` |

## 2. Threats

### STRIDE-LM Distribution

| Category | Findings |
|----------|----------|
| Spoofing | 9 |
| Tampering | 68 |
| Information Disclosure | 2 |

### Findings

#### 🟠 1. Dynamic Tool Loading - Tool Poisoning Risk

**Severity:** HIGH | **Risk Score:** 1.00

Dynamic tool/plugin loading detected at agent.py:92 - risk of tool poisoning

**STRIDE-LM:** Tampering — *Can I trust what I'm seeing?*

**Affected Locations:**

| File | Line | Asset | Type |
|------|------|-------|------|
| `agent.py` | 37 | File Operation | filesystem |
| `agent.py` | 51 | File Operation | filesystem |
| `agent.py` | 56 | File Operation | filesystem |
| `agent.py` | 64 | File Operation | filesystem |
| `agent.py` | 92 | Database Update | database |
| `agent.py` | 94 | Database Update | database |

**Mitigations:**

- **[high]** Sign all code and data
  ```
  // Implement appropriate security control
  ```
- **[high]** Implement software bill of materials (SBOM)
  ```
  // Implement appropriate security control
  ```

---

#### 🟠 2. LLM Integration - Prompt Injection Risk

**Severity:** HIGH | **Risk Score:** 1.00

LLM/AI framework detected at agent.py:11 - susceptible to prompt injection attacks

**STRIDE-LM:** Tampering — *Can I trust what I'm seeing?*

**Affected Locations:**

| File | Line | Asset | Type |
|------|------|-------|------|
| `agent.py` | 37 | File Operation | filesystem |
| `agent.py` | 51 | File Operation | filesystem |
| `agent.py` | 56 | File Operation | filesystem |
| `agent.py` | 64 | File Operation | filesystem |
| `agent.py` | 92 | Database Update | database |
| `agent.py` | 94 | Database Update | database |

**Mitigations:**

- **[high]** Sign all code and data
  ```
  // Implement appropriate security control
  ```
- **[high]** Implement software bill of materials (SBOM)
  ```
  // Implement appropriate security control
  ```

---

#### 🟠 3. Unvalidated Trust Boundary Crossing

**Severity:** HIGH | **Risk Score:** 1.00

Data crosses trust boundary from agent.py:19 to agent.py:25 without apparent validation

**STRIDE-LM:** Tampering — *Can I trust what I'm seeing?*

**Affected Locations:**

| File | Line | Asset | Type |
|------|------|-------|------|
| `agent.py` | 37 | File Operation | filesystem |
| `agent.py` | 51 | File Operation | filesystem |
| `agent.py` | 56 | File Operation | filesystem |
| `agent.py` | 64 | File Operation | filesystem |
| `agent.py` | 92 | Database Update | database |
| `agent.py` | 94 | Database Update | database |

**Mitigations:**

- **[high]** Sign all code and data
  ```
  // Implement appropriate security control
  ```
- **[high]** Implement software bill of materials (SBOM)
  ```
  // Implement appropriate security control
  ```

---

#### 🟡 4. Unvalidated Trust Boundary Crossing

**Severity:** MEDIUM | **Risk Score:** 1.00

Data crosses trust boundary from agent.py:81 to agent.py:11 without apparent validation

**STRIDE-LM:** Tampering — *Can I trust what I'm seeing?*

**Affected Locations:**

| File | Line | Asset | Type |
|------|------|-------|------|
| `agent.py` | 37 | File Operation | filesystem |
| `agent.py` | 51 | File Operation | filesystem |
| `agent.py` | 56 | File Operation | filesystem |
| `agent.py` | 64 | File Operation | filesystem |
| `agent.py` | 92 | Database Update | database |
| `agent.py` | 94 | Database Update | database |

**Mitigations:**

- **[medium]** Sign all code and data
  ```
  // Implement appropriate security control
  ```
- **[medium]** Implement software bill of materials (SBOM)
  ```
  // Implement appropriate security control
  ```

---

#### 🟡 5. Unvalidated Trust Boundary Crossing

**Severity:** MEDIUM | **Risk Score:** 1.00

Data crosses trust boundary from agent.py:19 to agent.py:37 without apparent validation

**STRIDE-LM:** Tampering — *Can I trust what I'm seeing?*

**Affected Locations:**

| File | Line | Asset | Type |
|------|------|-------|------|
| `agent.py` | 37 | File Operation | filesystem |
| `agent.py` | 51 | File Operation | filesystem |
| `agent.py` | 56 | File Operation | filesystem |
| `agent.py` | 64 | File Operation | filesystem |
| `agent.py` | 92 | Database Update | database |
| `agent.py` | 94 | Database Update | database |

**Mitigations:**

- **[medium]** Sign all code and data
  ```
  // Implement appropriate security control
  ```
- **[medium]** Implement software bill of materials (SBOM)
  ```
  // Implement appropriate security control
  ```

---

#### 🟡 6. Unvalidated Trust Boundary Crossing

**Severity:** MEDIUM | **Risk Score:** 1.00

Data crosses trust boundary from agent.py:19 to agent.py:92 without apparent validation

**STRIDE-LM:** Tampering — *Can I trust what I'm seeing?*

**Affected Locations:**

| File | Line | Asset | Type |
|------|------|-------|------|
| `agent.py` | 37 | File Operation | filesystem |
| `agent.py` | 51 | File Operation | filesystem |
| `agent.py` | 56 | File Operation | filesystem |
| `agent.py` | 64 | File Operation | filesystem |
| `agent.py` | 92 | Database Update | database |
| `agent.py` | 94 | Database Update | database |

**Mitigations:**

- **[medium]** Sign all code and data
  ```
  // Implement appropriate security control
  ```
- **[medium]** Implement software bill of materials (SBOM)
  ```
  // Implement appropriate security control
  ```

---

#### 🟡 7. Cryptographic Error Leakage

**Severity:** MEDIUM | **Risk Score:** 1.00

Cryptographic operation at agent.py:11 may leak errors or timing information (2 instances across 1 files)

**STRIDE-LM:** Information Disclosure — *What's escaping?*

**Affected Locations:**

| File | Line | Asset | Type |
|------|------|-------|------|
| `agent.py` | 19 | unknown | api |
| `agent.py` | 23 | unknown | api |
| `agent.py` | 81 | unknown | api |
| `agent.py` | 92 | Database Update | database |
| `agent.py` | 94 | Database Update | database |
| `agent.py` | 138 | unknown | api |
| `agent.py` | 140 | unknown | api |
| `agent.py` | 178 | unknown | api |
| `agent.py` | 190 | unknown | api |
| `agent.py` | 192 | unknown | api |

*...and 1 more locations*

**Mitigations:**

- **[medium]** Encrypt data at rest and in transit
  ```
  // Implement appropriate security control
  ```
- **[medium]** Implement secrets management systems
  ```
  // Implement appropriate security control
  ```

---

## 3. Mitigating Controls

### Recommended Actions (by priority)

| # | Priority | Control | Applies To |
|---|----------|---------|------------|
| 1 | 🟠 high | Sign all code and data | 36 threats |
| 2 | 🟠 high | Implement software bill of materials (SBOM) | 36 threats |
| 3 | 🟡 medium | Encrypt data at rest and in transit | 11 threats |
| 4 | 🟡 medium | Implement secrets management systems | 11 threats |

---

*Generated by [TITO](https://github.com/Leathal1/TITO) — Threat In, Threat Out*  
*Report date: 2026-02-05 09:21 UTC*
