# 17850930 - Castoff Point

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Foret de Hennetiel (ID: 262) |
| Block Size       | 2444 bytes                   |
| Total Events     | 4                            |
| References Count | 70                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [18](#event-18)       | 0x0001       |    632 |            131 |
| [512](#event-512)     | 0x0279       |    194 |             40 |
| [19](#event-19)       | 0x033B       |   1305 |            158 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0877      |        2167 |
|       2 | 0x089D      |        2205 |
|       3 | 0x1F0F      |        7951 |
|       4 | 0x0004      |           4 |
|       5 | 0x1F12      |        7954 |
|       6 | 0x0001      |           1 |
|       7 | 0x1F14      |        7956 |
|       8 | 0x1F15      |        7957 |
|       9 | 0x0005      |           5 |
|      10 | 0x0064      |         100 |
|      11 | 0x0065      |         101 |
|      12 | 0x00C8      |         200 |
|      13 | 0xFFFCA4A0  |  4294747296 |
|      14 | 0x38270     |      230000 |
|      15 | 0xFFFFFF01  |  4294967041 |
|      16 | 0x0C00      |        3072 |
|      17 | 0xFFFE5250  |  4294857296 |
|      18 | 0x222E0     |      140000 |
|      19 | 0xFFFFFF21  |  4294967073 |
|      20 | 0x0800      |        2048 |
|      21 | 0x0002      |           2 |
|      22 | 0xFFFFD8F0  |  4294957296 |
|      23 | 0xEA60      |       60000 |
|      24 | 0xFFFFFF00  |  4294967040 |
|      25 | 0x0003      |           3 |
|      26 | 0x4E20      |       20000 |
|      27 | 0xFFFEEE90  |  4294897296 |
|      28 | 0xFFFFFF20  |  4294967072 |
|      29 | 0x0400      |        1024 |
|      30 | 0x35B60     |      220000 |
|      31 | 0x249F0     |      150000 |
|      32 | 0x5CC60     |      380000 |
|      33 | 0xFFFDB610  |  4294817296 |
|      34 | 0xFFFFFF22  |  4294967074 |
|      35 | 0xFFFCBFCE  |  4294754254 |
|      36 | 0x372BB     |      225979 |
|      37 | 0xFFFFFFB3  |  4294967219 |
|      38 | 0x0BCE      |        3022 |
|      39 | 0xFFFFC1A2  |  4294951330 |
|      40 | 0xB6C1      |       46785 |
|      41 | 0xFFFFFE5A  |  4294966874 |
|      42 | 0x004A      |          74 |
|      43 | 0x37CD8     |      228568 |
|      44 | 0x23D04     |      146692 |
|      45 | 0xFFFFFF1E  |  4294967070 |
|      46 | 0x0D4D      |        3405 |
|      47 | 0x1F13      |        7955 |
|      48 | 0x6DDD0     |      450000 |
|      49 | 0xFFFF2928  |  4294912296 |
|      50 | 0xFFFFFC7C  |  4294966396 |
|      51 | 0xFFFFFC00  |  4294966272 |
|      52 | 0x77A10     |      490000 |
|      53 | 0xFFFDC5B0  |  4294821296 |
|      54 | 0xFFFFFBF9  |  4294966265 |
|      55 | 0x044C      |        1100 |
|      56 | 0x0013      |          19 |
|      57 | 0x0017      |          23 |
|      58 | 0x36EE8     |      225000 |
|      59 | 0x0320      |         800 |
|      60 | 0xFFFFC950  |  4294953296 |
|      61 | 0x23A50     |      146000 |
|      62 | 0x00F5      |         245 |
|      63 | 0x0078      |         120 |
|      64 | 0x001E      |          30 |
|      65 | 0x00A0      |         160 |
|      66 | 0x1F11      |        7953 |
|      67 | 0xFFFFF800  |  4294965248 |
|      68 | 0x005A      |          90 |
|      69 | 0x014A      |         330 |

## String References

- **7951**: You should be able to head [to the other side/over there] if you have the $3 and $3.
- **7953**: This river is not suitable for swimming.
- **7954**: Head [for the other side/over there]? [Yes./No./Dive right in.]
- **7955**: Gah! You lost control of your boat, sending you spiralling downstream!
- **7956**: Head in which direction? [Upstream./Downstream.]
- **7957**: You cannot proceed any farther [upstream/downstream].

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 632 bytes |
| Instructions | 122       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 04 10 00 80 03 06  10 01 80 03 05 10 02 80   ...............
0010: 48 03 80 23 03 04 10 00  80 02 03 10 00 80 02 29  H..#...........)
0020: 00 03 03 10 04 80 01 2E  00 03 03 10 00 80 24 05  ..............$.
0030: 80 00 80 03 10 25 02 00  10 00 80 00 FC 01 02 02  .....%..........
0040: 10 00 80 80 84 00 03 03  10 06 80 24 07 80 00 80  ...........$....
0050: 00 80 25 02 00 10 00 80  00 69 00 03 02 10 00 80  ..%......i......
0060: 48 08 80 23 21 00 01 81  00 02 00 10 06 80 00 81  H..#!...........
0070: 00 03 06 10 00 80 42 43  00 43 01 1A B5 06 01 81  ......BC.C......
0080: 00 01 2D 01 02 02 10 09  80 80 CA 00 03 03 10 04  ..-.............
0090: 80 24 07 80 00 80 00 80  25 02 00 10 00 80 00 B1  .$......%.......
00A0: 00 03 06 10 06 80 42 43  00 43 01 1A B5 06 01 C7  ......BC.C......
00B0: 00 02 00 10 06 80 00 C7  00 03 02 10 06 80 48 08  ..............H.
00C0: 80 23 21 00 01 C7 00 01  2D 01 02 02 10 0A 80 80  .#!.....-.......
00D0: DA 00 03 03 10 0B 80 01  2D 01 02 02 10 0B 80 80  ........-.......
00E0: EA 00 03 03 10 0A 80 01  2D 01 03 03 10 02 10 24  ........-......$
00F0: 07 80 00 80 00 80 25 02  00 10 00 80 00 12 01 0C  ......%.........
0100: 03 10 03 06 10 06 80 42  43 00 43 01 1A B5 06 01  .......BC.C.....
0110: 2D 01 02 00 10 06 80 00  2D 01 0B 03 10 03 06 10  -.......-.......
0120: 00 80 42 43 00 43 01 1A  B5 06 01 2D 01 45 0C 80  ..BC.C.....-.E..
0130: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 00 80 55 0C  ........fdo1..U.
0140: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 03 10  .........fdo1...
0150: 00 80 80 64 01 47 00 0D  80 0E 80 0F 80 10 80 47  ...d.G.........G
0160: 01 01 D7 01 02 03 10 06  80 80 7B 01 47 00 11 80  ..........{.G...
0170: 12 80 13 80 14 80 47 01  01 D7 01 02 03 10 15 80  ......G.........
0180: 80 92 01 47 00 16 80 17  80 18 80 00 80 47 01 01  ...G.........G..
0190: D7 01 02 03 10 19 80 80  A9 01 47 00 1A 80 1B 80  ..........G.....
01A0: 1C 80 1D 80 47 01 01 D7  01 02 03 10 04 80 80 C0  ....G...........
01B0: 01 47 00 1E 80 1F 80 0F  80 10 80 47 01 01 D7 01  .G.........G....
01C0: 02 03 10 09 80 80 D7 01  47 00 20 80 21 80 22 80  ........G. .!.".
01D0: 1D 80 47 01 01 D7 01 46  00 45 0C 80 F0 FF FF 7F  ..G....F.E......
01E0: F0 FF FF 7F 66 64 69 31  00 80 55 0C 80 F0 FF FF  ....fdi1..U.....
01F0: 7F F0 FF FF 7F 66 64 69  31 01 77 02 02 00 10 06  .....fdi1.w.....
0200: 80 00 07 02 01 77 02 02  00 10 15 80 00 77 02 42  .....w.......w.B
0210: 43 00 43 01 1A 73 04 02  02 10 00 80 80 2E 02 47  C.C..s.........G
0220: 00 23 80 24 80 25 80 26  80 47 01 01 5C 02 02 02  .#.$.%.&.G..\...
0230: 10 15 80 80 45 02 47 00  27 80 28 80 29 80 2A 80  ....E.G.'.(.).*.
0240: 47 01 01 5C 02 02 02 10  04 80 80 5C 02 47 00 2B  G..\.......\.G.+
0250: 80 2C 80 2D 80 2E 80 47  01 01 5C 02 46 00 45 0C  .,.-...G..\.F.E.
0260: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 32 00 80 03  .........fdi2...
0270: 01 10 19 80 01 77 02 21  00                       .....w.!.       
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[4] = 0*
  1: 0x0006 [0x03] Work_Zone[6] = 2167*
  2: 0x000B [0x03] Work_Zone[5] = 2205*
  3: 0x0010 [0x48] [System] [7951*]:
    → "You should be able to head [to the other side/over there] if you have the $3 and $3."
  4: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0014 [0x03] Work_Zone[4] = 0*
  6: 0x0019 [0x02] IF !(Work_Zone[3] <= 0*) GOTO 0x0029
  7: 0x0021 [0x03] Work_Zone[3] = 4*
  8: 0x0026 [0x01] GOTO 0x002E
  9: 0x0029 [0x03] Work_Zone[3] = 0*

SUBROUTINE_002E:
 10: 0x002E [0x24] CREATE_DIALOG(message_id=7954*, default_option=0*, option_flags=Work_Zone[3])
    → "Head [for the other side/over there]? [Yes./No./Dive right in.]"
 11: 0x0035 [0x25] WAIT_DIALOG_SELECT()
 12: 0x0036 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01FC
 13: 0x003E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0084
 14: 0x0046 [0x03] Work_Zone[3] = 1*
 15: 0x004B [0x24] CREATE_DIALOG(message_id=7956*, default_option=0*, option_flags=0*)
    → "Head in which direction? [Upstream./Downstream.]"
 16: 0x0052 [0x25] WAIT_DIALOG_SELECT()
 17: 0x0053 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0069
 18: 0x005B [0x03] Work_Zone[2] = 0*
 19: 0x0060 [0x48] [System] [7957*]:
    → "You cannot proceed any farther [upstream/downstream]."
 20: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0064 [0x21] END_EVENT
 22: 0x0065 [0x00] END_REQSTACK()

SUBROUTINE_0081:
 23: 0x0081 [0x01] GOTO 0x012D
 24: 0x0084 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x00CA
 25: 0x008C [0x03] Work_Zone[3] = 4*
 26: 0x0091 [0x24] CREATE_DIALOG(message_id=7956*, default_option=0*, option_flags=0*)
    → "Head in which direction? [Upstream./Downstream.]"
 27: 0x0098 [0x25] WAIT_DIALOG_SELECT()
 28: 0x0099 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00B1
 29: 0x00A1 [0x03] Work_Zone[6] = 1*
 30: 0x00A6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 31: 0x00A7 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 32: 0x00A9 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 33: 0x00AB [0x1A] CALL_SUBROUTINE(address=0x06B5)
 34: 0x00AE [0x01] GOTO 0x00C7
 35: 0x00B1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00C7
 36: 0x00B9 [0x03] Work_Zone[2] = 1*
 37: 0x00BE [0x48] [System] [7957*]:
    → "You cannot proceed any farther [upstream/downstream]."
 38: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x00C2 [0x21] END_EVENT
 40: 0x00C3 [0x00] END_REQSTACK()

SUBROUTINE_00C7:
 41: 0x00C7 [0x01] GOTO 0x012D
 42: 0x00CA [0x02] IF !(Work_Zone[2] == 100*) GOTO 0x00DA
 43: 0x00D2 [0x03] Work_Zone[3] = 101*
 44: 0x00D7 [0x01] GOTO 0x012D
 45: 0x00DA [0x02] IF !(Work_Zone[2] == 101*) GOTO 0x00EA
 46: 0x00E2 [0x03] Work_Zone[3] = 100*
 47: 0x00E7 [0x01] GOTO 0x012D
 48: 0x00EA [0x03] Work_Zone[3] = Work_Zone[2]
 49: 0x00EF [0x24] CREATE_DIALOG(message_id=7956*, default_option=0*, option_flags=0*)
    → "Head in which direction? [Upstream./Downstream.]"
 50: 0x00F6 [0x25] WAIT_DIALOG_SELECT()
 51: 0x00F7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0112
 52: 0x00FF [0x0C] Work_Zone[3]--
 53: 0x0102 [0x03] Work_Zone[6] = 1*
 54: 0x0107 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 55: 0x0108 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 56: 0x010A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 57: 0x010C [0x1A] CALL_SUBROUTINE(address=0x06B5)
 58: 0x010F [0x01] GOTO 0x012D
 59: 0x0112 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x012D
 60: 0x011A [0x0B] Work_Zone[3]++
 61: 0x011D [0x03] Work_Zone[6] = 0*
 62: 0x0122 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 63: 0x0123 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 64: 0x0125 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 65: 0x0127 [0x1A] CALL_SUBROUTINE(address=0x06B5)
 66: 0x012A [0x01] GOTO 0x012D

SUBROUTINE_012D:
 67: 0x012D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 68: 0x013E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 69: 0x014D [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0164
 70: 0x0155 [0x47] UPDATE_PLAYER_POS(-220.000*, 230.000*, -0.255*, yaw=270.0°*)
 71: 0x015F [0x47] WAIT_PLAYER_POS_UPDATE
 72: 0x0161 [0x01] GOTO 0x01D7
 73: 0x0164 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x017B
 74: 0x016C [0x47] UPDATE_PLAYER_POS(-110.000*, 140.000*, -0.223*, yaw=180.0°*)
 75: 0x0176 [0x47] WAIT_PLAYER_POS_UPDATE
 76: 0x0178 [0x01] GOTO 0x01D7
 77: 0x017B [0x02] IF !(Work_Zone[3] == 2*) GOTO 0x0192
 78: 0x0183 [0x47] UPDATE_PLAYER_POS(-10.000*, 60.000*, -0.256*, yaw=0.0°*)
 79: 0x018D [0x47] WAIT_PLAYER_POS_UPDATE
 80: 0x018F [0x01] GOTO 0x01D7
 81: 0x0192 [0x02] IF !(Work_Zone[3] == 3*) GOTO 0x01A9
 82: 0x019A [0x47] UPDATE_PLAYER_POS(20.000*, -70.000*, -0.224*, yaw=90.0°*)
 83: 0x01A4 [0x47] WAIT_PLAYER_POS_UPDATE
 84: 0x01A6 [0x01] GOTO 0x01D7
 85: 0x01A9 [0x02] IF !(Work_Zone[3] == 4*) GOTO 0x01C0
 86: 0x01B1 [0x47] UPDATE_PLAYER_POS(220.000*, 150.000*, -0.255*, yaw=270.0°*)
 87: 0x01BB [0x47] WAIT_PLAYER_POS_UPDATE
 88: 0x01BD [0x01] GOTO 0x01D7
 89: 0x01C0 [0x02] IF !(Work_Zone[3] == 5*) GOTO 0x01D7
 90: 0x01C8 [0x47] UPDATE_PLAYER_POS(380.000*, -150.000*, -0.222*, yaw=90.0°*)
 91: 0x01D2 [0x47] WAIT_PLAYER_POS_UPDATE
 92: 0x01D4 [0x01] GOTO 0x01D7

SUBROUTINE_01D7:
 93: 0x01D7 [0x46] CAMERA_CONTROL: Restore default settings
 94: 0x01D9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 95: 0x01EA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 96: 0x01F9 [0x01] GOTO 0x0277
 97: 0x01FC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0207
 98: 0x0204 [0x01] GOTO 0x0277
 99: 0x0207 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0277
100: 0x020F [0x42] SET_CLI_EVENT_CANCEL_DATA()
101: 0x0210 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
102: 0x0212 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
103: 0x0214 [0x1A] CALL_SUBROUTINE(address=0x0473)
104: 0x0217 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x022E
105: 0x021F [0x47] UPDATE_PLAYER_POS(-213.042*, 225.979*, -0.077*, yaw=265.6°*)
106: 0x0229 [0x47] WAIT_PLAYER_POS_UPDATE
107: 0x022B [0x01] GOTO 0x025C
108: 0x022E [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0245
109: 0x0236 [0x47] UPDATE_PLAYER_POS(-15.966*, 46.785*, -0.422*, yaw=6.5°*)
110: 0x0240 [0x47] WAIT_PLAYER_POS_UPDATE
111: 0x0242 [0x01] GOTO 0x025C
112: 0x0245 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x025C
113: 0x024D [0x47] UPDATE_PLAYER_POS(228.568*, 146.692*, -0.226*, yaw=299.3°*)
114: 0x0257 [0x47] WAIT_PLAYER_POS_UPDATE
115: 0x0259 [0x01] GOTO 0x025C

SUBROUTINE_025C:
116: 0x025C [0x46] CAMERA_CONTROL: Restore default settings
117: 0x025E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
118: 0x026F [0x03] Work_Zone[1] = 3*
119: 0x0274 [0x01] GOTO 0x0277

SUBROUTINE_0277:
120: 0x0277 [0x21] END_EVENT
121: 0x0278 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0066 [0x01] GOTO 0x0081
# Dead code (unreachable instructions):
     0x00C4 [0x01] GOTO 0x00C7
```

### Event 512

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0279    |
| Data Size    | 194 bytes |
| Instructions | 40        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                             03 04 10 00 80 03 06           .......
0280: 10 01 80 03 05 10 02 80  48 03 80 23 03 04 10 00  ........H..#....
0290: 80 02 03 10 00 80 02 9C  02 01 39 03 03 03 10 06  ..........9.....
02A0: 80 24 05 80 00 80 03 10  25 02 00 10 00 80 00 B9  .$......%.......
02B0: 02 03 01 10 06 80 01 39  03 02 00 10 06 80 00 C9  .......9........
02C0: 02 03 01 10 15 80 01 39  03 02 00 10 15 80 00 39  .......9.......9
02D0: 03 42 43 00 43 01 1A 73  04 02 02 10 00 80 80 F0  .BC.C..s........
02E0: 02 47 00 23 80 24 80 25  80 26 80 47 01 01 1E 03  .G.#.$.%.&.G....
02F0: 02 02 10 15 80 80 07 03  47 00 27 80 28 80 29 80  ........G.'.(.).
0300: 2A 80 47 01 01 1E 03 02  02 10 04 80 80 1E 03 47  *.G............G
0310: 00 2B 80 2C 80 2D 80 2E  80 47 01 01 1E 03 46 00  .+.,.-...G....F.
0320: 45 0C 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 32 00  E..........fdi2.
0330: 80 03 01 10 19 80 01 39  03 21 00                 .......9.!.     
```

#### Opcodes

```
  0: 0x0279 [0x03] Work_Zone[4] = 0*
  1: 0x027E [0x03] Work_Zone[6] = 2167*
  2: 0x0283 [0x03] Work_Zone[5] = 2205*
  3: 0x0288 [0x48] [System] [7951*]:
    → "You should be able to head [to the other side/over there] if you have the $3 and $3."
  4: 0x028B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x028C [0x03] Work_Zone[4] = 0*
  6: 0x0291 [0x02] IF !(Work_Zone[3] <= 0*) GOTO 0x029C
  7: 0x0299 [0x01] GOTO 0x0339
  8: 0x029C [0x03] Work_Zone[3] = 1*
  9: 0x02A1 [0x24] CREATE_DIALOG(message_id=7954*, default_option=0*, option_flags=Work_Zone[3])
    → "Head [for the other side/over there]? [Yes./No./Dive right in.]"
 10: 0x02A8 [0x25] WAIT_DIALOG_SELECT()
 11: 0x02A9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02B9
 12: 0x02B1 [0x03] Work_Zone[1] = 1*
 13: 0x02B6 [0x01] GOTO 0x0339
 14: 0x02B9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02C9
 15: 0x02C1 [0x03] Work_Zone[1] = 2*
 16: 0x02C6 [0x01] GOTO 0x0339
 17: 0x02C9 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0339
 18: 0x02D1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 19: 0x02D2 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 20: 0x02D4 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 21: 0x02D6 [0x1A] CALL_SUBROUTINE(address=0x0473)
 22: 0x02D9 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x02F0
 23: 0x02E1 [0x47] UPDATE_PLAYER_POS(-213.042*, 225.979*, -0.077*, yaw=265.6°*)
 24: 0x02EB [0x47] WAIT_PLAYER_POS_UPDATE
 25: 0x02ED [0x01] GOTO 0x031E
 26: 0x02F0 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0307
 27: 0x02F8 [0x47] UPDATE_PLAYER_POS(-15.966*, 46.785*, -0.422*, yaw=6.5°*)
 28: 0x0302 [0x47] WAIT_PLAYER_POS_UPDATE
 29: 0x0304 [0x01] GOTO 0x031E
 30: 0x0307 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x031E
 31: 0x030F [0x47] UPDATE_PLAYER_POS(228.568*, 146.692*, -0.226*, yaw=299.3°*)
 32: 0x0319 [0x47] WAIT_PLAYER_POS_UPDATE
 33: 0x031B [0x01] GOTO 0x031E

SUBROUTINE_031E:
 34: 0x031E [0x46] CAMERA_CONTROL: Restore default settings
 35: 0x0320 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 36: 0x0331 [0x03] Work_Zone[1] = 3*
 37: 0x0336 [0x01] GOTO 0x0339

SUBROUTINE_0339:
 38: 0x0339 [0x21] END_EVENT
 39: 0x033A [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x033B     |
| Data Size    | 1305 bytes |
| Instructions | 118        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0330:                                   03 04 10 00 80             .....
0340: 03 06 10 01 80 03 05 10  02 80 48 03 80 23 03 04  ..........H..#..
0350: 10 00 80 02 03 10 00 80  02 63 03 03 03 10 04 80  .........c......
0360: 01 68 03 03 03 10 00 80  24 05 80 00 80 03 10 25  .h......$......%
0370: 02 00 10 00 80 00 F1 03  42 43 00 43 01 45 0C 80  ........BC.C.E..
0380: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 00 80 55 0C  ........fdo1..U.
0390: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 48 2F 80  .........fdo1H/.
03A0: 23 0D 02 10 06 80 02 02  10 06 80 00 BD 03 47 00  #.............G.
03B0: 30 80 31 80 32 80 33 80  47 01 01 C9 03 47 00 34  0.1.2.3.G....G.4
03C0: 80 35 80 36 80 37 80 47  01 45 0C 80 F0 FF FF 7F  .5.6.7.G.E......
03D0: F0 FF FF 7F 66 64 69 31  00 80 55 0C 80 F0 FF FF  ....fdi1..U.....
03E0: 7F F0 FF FF 7F 66 64 69  31 03 01 10 06 80 01 71  .....fdi1......q
03F0: 04 02 00 10 06 80 00 01  04 03 01 10 15 80 01 71  ...............q
0400: 04 02 00 10 15 80 00 71  04 42 43 00 43 01 1A 73  .......q.BC.C..s
0410: 04 02 02 10 00 80 80 28  04 47 00 23 80 24 80 25  .......(.G.#.$.%
0420: 80 26 80 47 01 01 56 04  02 02 10 15 80 80 3F 04  .&.G..V.......?.
0430: 47 00 27 80 28 80 29 80  2A 80 47 01 01 56 04 02  G.'.(.).*.G..V..
0440: 02 10 04 80 80 56 04 47  00 2B 80 2C 80 2D 80 2E  .....V.G.+.,.-..
0450: 80 47 01 01 56 04 46 00  45 0C 80 F0 FF FF 7F F0  .G..V.F.E.......
0460: FF FF 7F 66 64 69 32 00  80 03 01 10 19 80 01 71  ...fdi2........q
0470: 04 21 00 45 0C 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .!.E..........fd
0480: 6F 31 00 80 55 0C 80 F0  FF FF 7F F0 FF FF 7F 66  o1..U..........f
0490: 64 6F 31 46 01 38 38 80  4E 01 F0 FF FF 7F 02 02  do1F.88.N.......
04A0: 10 00 80 80 C7 04 45 39  80 F0 FF FF 7F F0 FF FF  ......E9........
04B0: 7F 73 30 30 31 00 80 BA  32 62 10 01 0D 80 3A 80  .s001...2b....:.
04C0: 3B 80 26 80 01 19 05 02  02 10 15 80 80 F0 04 45  ;.&............E
04D0: 39 80 F0 FF FF 7F F0 FF  FF 7F 73 31 30 31 00 80  9.........s101..
04E0: BA 32 62 10 01 3C 80 17  80 3B 80 26 80 01 19 05  .2b..<...;.&....
04F0: 02 02 10 04 80 80 19 05  45 39 80 F0 FF FF 7F F0  ........E9......
0500: FF FF 7F 73 32 30 31 00  80 BA 32 62 10 01 1E 80  ...s201...2b....
0510: 3D 80 3B 80 26 80 01 19  05 45 0C 80 F0 FF FF 7F  =.;.&....E......
0520: F0 FF FF 7F 66 64 69 31  00 80 45 39 80 F0 FF FF  ....fdi1..E9....
0530: 7F F0 FF FF 7F 64 62 6E  30 00 80 9F 3E 80 F8 FF  .....dbn0...>...
0540: FF 7F F8 FF FF 7F 73 74  72 30 00 80 1C 3F 80 45  ......str0...?.E
0550: 0C 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 00 80  ..........fdo1..
0560: 55 0C 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  U..........fdo1.
0570: 02 10 00 80 80 89 05 52  39 80 F0 FF FF 7F F0 FF  .......R9.......
0580: FF 7F 73 30 30 31 01 BD  05 02 02 10 15 80 80 A3  ..s001..........
0590: 05 52 39 80 F0 FF FF 7F  F0 FF FF 7F 73 31 30 31  .R9.........s101
05A0: 01 BD 05 02 02 10 04 80  80 BD 05 52 39 80 F0 FF  ...........R9...
05B0: FF 7F F0 FF FF 7F 73 32  30 31 01 BD 05 4E 00 F0  ......s201...N..
05C0: FF FF 7F 02 02 10 00 80  80 DB 05 BA F0 FF FF 7F  ................
05D0: 23 80 24 80 25 80 26 80  01 0B 06 02 02 10 15 80  #.$.%.&.........
05E0: 80 F3 05 BA F0 FF FF 7F  27 80 28 80 29 80 2A 80  ........'.(.).*.
05F0: 01 0B 06 02 02 10 04 80  80 0B 06 BA F0 FF FF 7F  ................
0600: 2B 80 2C 80 2D 80 2E 80  01 0B 06 2C F0 FF FF 7F  +.,.-......,....
0610: F0 FF FF 7F 63 6F 72 70  53 F0 FF FF 7F F0 FF FF  ....corpS.......
0620: 7F 63 6F 72 70 1C 40 80  02 02 10 00 80 80 44 06  .corp.@.......D.
0630: 45 39 80 F0 FF FF 7F F0  FF FF 7F 73 30 30 32 00  E9.........s002.
0640: 80 01 7C 06 02 02 10 15  80 80 60 06 45 39 80 F0  ..|.......`.E9..
0650: FF FF 7F F0 FF FF 7F 73  31 30 32 00 80 01 7C 06  .......s102...|.
0660: 02 02 10 04 80 80 7C 06  45 39 80 F0 FF FF 7F F0  ......|.E9......
0670: FF FF 7F 73 32 30 32 00  80 01 7C 06 45 0C 80 F0  ...s202...|.E...
0680: FF FF 7F F0 FF FF 7F 66  64 69 32 00 80 1C 41 80  .......fdi2...A.
0690: 45 0C 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 00  E..........fdo1.
06A0: 80 55 0C 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .U..........fdo1
06B0: 48 42 80 23 1B 45 0C 80  F0 FF FF 7F F0 FF FF 7F  HB.#.E..........
06C0: 66 64 6F 31 00 80 55 0C  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
06D0: 7F 66 64 6F 31 46 01 38  38 80 BA F0 FF FF 7F 16  .fdo1F.88.......
06E0: 80 17 80 2D 80 43 80 45  39 80 F0 FF FF 7F F0 FF  ...-.C.E9.......
06F0: FF 7F 73 30 30 33 00 80  45 0C 80 F0 FF FF 7F F0  ..s003..E.......
0700: FF FF 7F 66 64 69 32 00  80 1C 40 80 27 10 F0 FF  ...fdi2...@.'...
0710: FF 7F 12 1C 44 80 45 0C  80 F0 FF FF 7F F0 FF FF  ....D.E.........
0720: 7F 66 64 6F 31 00 80 55  0C 80 F0 FF FF 7F F0 FF  .fdo1..U........
0730: FF 7F 66 64 6F 31 2A 10  F0 FF FF 7F 29 10 39 62  ..fdo1*.....).9b
0740: 10 01 02 52 39 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...R9.........s0
0750: 30 33 45 39 80 F0 FF FF  7F F0 FF FF 7F 73 30 30  03E9.........s00
0760: 34 00 80 45 0C 80 F0 FF  FF 7F F0 FF FF 7F 66 64  4..E..........fd
0770: 69 32 00 80 1C 40 80 27  10 F0 FF FF 7F 13 1C 44  i2...@.'.......D
0780: 80 45 0C 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0790: 00 80 55 0C 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
07A0: 31 2A 10 F0 FF FF 7F 52  39 80 F0 FF FF 7F F0 FF  1*.....R9.......
07B0: FF 7F 73 30 30 34 29 10  39 62 10 01 03 02 06 10  ..s004).9b......
07C0: 06 80 00 D9 07 45 39 80  F0 FF FF 7F F0 FF FF 7F  .....E9.........
07D0: 73 30 30 39 00 80 01 EA  07 45 39 80 F0 FF FF 7F  s009.....E9.....
07E0: F0 FF FF 7F 73 30 30 38  00 80 4E 01 F0 FF FF 7F  ....s008..N.....
07F0: 45 0C 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 32 00  E..........fdi2.
0800: 80 1C 45 80 45 0C 80 F0  FF FF 7F F0 FF FF 7F 66  ..E.E..........f
0810: 64 6F 31 00 80 55 0C 80  F0 FF FF 7F F0 FF FF 7F  do1..U..........
0820: 66 64 6F 31 02 06 10 06  80 00 3E 08 52 39 80 F0  fdo1......>.R9..
0830: FF FF 7F F0 FF FF 7F 73  30 30 39 01 4D 08 52 39  .......s009.M.R9
0840: 80 F0 FF FF 7F F0 FF FF  7F 73 30 30 38 4E 00 F0  .........s008N..
0850: FF FF 7F 1B                                       ....            
```

#### Opcodes

```
  0: 0x033B [0x03] Work_Zone[4] = 0*
  1: 0x0340 [0x03] Work_Zone[6] = 2167*
  2: 0x0345 [0x03] Work_Zone[5] = 2205*
  3: 0x034A [0x48] [System] [7951*]:
    → "You should be able to head [to the other side/over there] if you have the $3 and $3."
  4: 0x034D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x034E [0x03] Work_Zone[4] = 0*
  6: 0x0353 [0x02] IF !(Work_Zone[3] <= 0*) GOTO 0x0363
  7: 0x035B [0x03] Work_Zone[3] = 4*
  8: 0x0360 [0x01] GOTO 0x0368
  9: 0x0363 [0x03] Work_Zone[3] = 0*

SUBROUTINE_0368:
 10: 0x0368 [0x24] CREATE_DIALOG(message_id=7954*, default_option=0*, option_flags=Work_Zone[3])
    → "Head [for the other side/over there]? [Yes./No./Dive right in.]"
 11: 0x036F [0x25] WAIT_DIALOG_SELECT()
 12: 0x0370 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03F1
 13: 0x0378 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x0379 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 15: 0x037B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 16: 0x037D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x038E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 18: 0x039D [0x48] [System] [7955*]:
    → "Gah! You lost control of your boat, sending you spiralling downstream!"
 19: 0x03A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x03A1 [0x0D] Work_Zone[2] &= 1*
 21: 0x03A6 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x03BD
 22: 0x03AE [0x47] UPDATE_PLAYER_POS(450.000*, -55.000*, -0.900*, yaw=377476129.2°*)
 23: 0x03B8 [0x47] WAIT_PLAYER_POS_UPDATE
 24: 0x03BA [0x01] GOTO 0x03C9
 25: 0x03BD [0x47] UPDATE_PLAYER_POS(490.000*, -146.000*, -1.031*, yaw=96.7°*)
 26: 0x03C7 [0x47] WAIT_PLAYER_POS_UPDATE

SUBROUTINE_03C9:
 27: 0x03C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x03DA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 29: 0x03E9 [0x03] Work_Zone[1] = 1*
 30: 0x03EE [0x01] GOTO 0x0471
 31: 0x03F1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0401
 32: 0x03F9 [0x03] Work_Zone[1] = 2*
 33: 0x03FE [0x01] GOTO 0x0471
 34: 0x0401 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0471
 35: 0x0409 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 36: 0x040A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 37: 0x040C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 38: 0x040E [0x1A] CALL_SUBROUTINE(address=0x0473)
 39: 0x0411 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0428
 40: 0x0419 [0x47] UPDATE_PLAYER_POS(-213.042*, 225.979*, -0.077*, yaw=265.6°*)
 41: 0x0423 [0x47] WAIT_PLAYER_POS_UPDATE
 42: 0x0425 [0x01] GOTO 0x0456
 43: 0x0428 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x043F
 44: 0x0430 [0x47] UPDATE_PLAYER_POS(-15.966*, 46.785*, -0.422*, yaw=6.5°*)
 45: 0x043A [0x47] WAIT_PLAYER_POS_UPDATE
 46: 0x043C [0x01] GOTO 0x0456
 47: 0x043F [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0456
 48: 0x0447 [0x47] UPDATE_PLAYER_POS(228.568*, 146.692*, -0.226*, yaw=299.3°*)
 49: 0x0451 [0x47] WAIT_PLAYER_POS_UPDATE
 50: 0x0453 [0x01] GOTO 0x0456

SUBROUTINE_0456:
 51: 0x0456 [0x46] CAMERA_CONTROL: Restore default settings
 52: 0x0458 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 53: 0x0469 [0x03] Work_Zone[1] = 3*
 54: 0x046E [0x01] GOTO 0x0471

SUBROUTINE_0471:
 55: 0x0471 [0x21] END_EVENT
 56: 0x0472 [0x00] END_REQSTACK()

SUBROUTINE_0473:
 57: 0x0473 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 58: 0x0484 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 59: 0x0493 [0x46] CAMERA_CONTROL: Disable user control
 60: 0x0495 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 61: 0x0498 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
 62: 0x049E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x04C7
 63: 0x04A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
 64: 0x04B7 [0xBA] SET_ENTITY_POSITION(entity_id=Castoff Point (ID: 17850930/0x01106232), pos_x=-220.000*, pos_z=225.000*, pos_y=0.800*, direction=265.6°*)
 65: 0x04C4 [0x01] GOTO 0x0519
 66: 0x04C7 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x04F0
 67: 0x04CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s101" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
 68: 0x04E0 [0xBA] SET_ENTITY_POSITION(entity_id=Castoff Point (ID: 17850930/0x01106232), pos_x=-14.000*, pos_z=60.000*, pos_y=0.800*, direction=265.6°*)
 69: 0x04ED [0x01] GOTO 0x0519
 70: 0x04F0 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0519
 71: 0x04F8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s201" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
 72: 0x0509 [0xBA] SET_ENTITY_POSITION(entity_id=Castoff Point (ID: 17850930/0x01106232), pos_x=220.000*, pos_z=146.000*, pos_y=0.800*, direction=265.6°*)
 73: 0x0516 [0x01] GOTO 0x0519

SUBROUTINE_0519:
 74: 0x0519 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 75: 0x052A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dbn0" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
 76: 0x053B [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "str0" with entities [EventEntity, EventEntity], work=[245*, 0*]
 77: 0x054C [0x1C] WAIT(120* ticks)
 78: 0x054F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 79: 0x0560 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 80: 0x056F [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0589
 81: 0x0577 [0x52] END_LOAD_SCHEDULER: End scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=23*
 82: 0x0586 [0x01] GOTO 0x05BD
 83: 0x0589 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x05A3
 84: 0x0591 [0x52] END_LOAD_SCHEDULER: End scheduler "s101" with entities [LocalPlayer, LocalPlayer], work=23*
 85: 0x05A0 [0x01] GOTO 0x05BD
 86: 0x05A3 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x05BD
 87: 0x05AB [0x52] END_LOAD_SCHEDULER: End scheduler "s201" with entities [LocalPlayer, LocalPlayer], work=23*
 88: 0x05BA [0x01] GOTO 0x05BD

SUBROUTINE_05BD:
 89: 0x05BD [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 90: 0x05C3 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x05DB
 91: 0x05CB [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-213.042*, pos_z=225.979*, pos_y=-0.077*, direction=265.6°*)
 92: 0x05D8 [0x01] GOTO 0x060B
 93: 0x05DB [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x05F3
 94: 0x05E3 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-15.966*, pos_z=46.785*, pos_y=-0.422*, direction=6.5°*)
 95: 0x05F0 [0x01] GOTO 0x060B
 96: 0x05F3 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x060B
 97: 0x05FB [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=228.568*, pos_z=146.692*, pos_y=-0.226*, direction=299.3°*)
 98: 0x0608 [0x01] GOTO 0x060B

SUBROUTINE_060B:
 99: 0x060B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [LocalPlayer, LocalPlayer]
100: 0x0618 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "corp" with entities [LocalPlayer, LocalPlayer]
101: 0x0625 [0x1C] WAIT(30* ticks)
102: 0x0628 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0644
103: 0x0630 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s002" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
104: 0x0641 [0x01] GOTO 0x067C
105: 0x0644 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0660
106: 0x064C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s102" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
107: 0x065D [0x01] GOTO 0x067C
108: 0x0660 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x067C
109: 0x0668 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s202" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
110: 0x0679 [0x01] GOTO 0x067C

SUBROUTINE_067C:
111: 0x067C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
112: 0x068D [0x1C] WAIT(160* ticks)
113: 0x0690 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
114: 0x06A1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
115: 0x06B0 [0x48] [System] [7953*]:
    → "This river is not suitable for swimming."
116: 0x06B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
117: 0x06B4 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x06B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x06C6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x06D5 [0x46] CAMERA_CONTROL: Disable user control
     0x06D7 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
     0x06DA [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-10.000*, pos_z=60.000*, pos_y=-0.226*, direction=377476039.2°*)
     0x06E7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s003" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
     0x06F8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0709 [0x1C] WAIT(30* ticks)
     0x070C [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x12)
     0x0713 [0x1C] WAIT(90* ticks)
     0x0716 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0727 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0736 [0x2A] GET_REQ_LEVEL(level=16, entity_id=LocalPlayer)
     0x073C [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Unnamed NPC (ID: 17850937/0x01106239), tag_num=0x02)
     0x0743 [0x52] END_LOAD_SCHEDULER: End scheduler "s003" with entities [LocalPlayer, LocalPlayer], work=23*
     0x0752 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s004" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
     0x0763 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0774 [0x1C] WAIT(30* ticks)
     0x0777 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x13)
     0x077E [0x1C] WAIT(90* ticks)
     0x0781 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0792 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x07A1 [0x2A] GET_REQ_LEVEL(level=16, entity_id=LocalPlayer)
     0x07A7 [0x52] END_LOAD_SCHEDULER: End scheduler "s004" with entities [LocalPlayer, LocalPlayer], work=23*
     0x07B6 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Unnamed NPC (ID: 17850937/0x01106239), tag_num=0x03)
     0x07BD [0x02] IF !(Work_Zone[6] == 1*) GOTO 0x07D9
     0x07C5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s009" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
     0x07D6 [0x01] GOTO 0x07EA
     0x07D9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s008" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
     0x07EA [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
     0x07F0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0801 [0x1C] WAIT(330* ticks)
     0x0804 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0815 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0824 [0x02] IF !(Work_Zone[6] == 1*) GOTO 0x083E
     0x082C [0x52] END_LOAD_SCHEDULER: End scheduler "s009" with entities [LocalPlayer, LocalPlayer], work=23*
     0x083B [0x01] GOTO 0x084D
     0x083E [0x52] END_LOAD_SCHEDULER: End scheduler "s008" with entities [LocalPlayer, LocalPlayer], work=23*
     0x084D [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
     0x0853 [0x1B] RETURN
```
