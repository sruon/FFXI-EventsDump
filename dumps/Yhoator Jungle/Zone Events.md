# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Yhoator Jungle (ID: 124) |
| Block Size       | 772 bytes                |
| Total Events     | 4                        |
| References Count | 21                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [105](#event-105)     | 0x0002       |    105 |             19 |
| [109](#event-109)     | 0x006B       |    549 |             75 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0029      |          41 |
|       1 | 0x00C9      |         201 |
|       2 | 0x0000      |           0 |
|       3 | 0x003C      |          60 |
|       4 | 0x001E      |          30 |
|       5 | 0x1E3E      |        7742 |
|       6 | 0x0027      |          39 |
|       7 | 0x00C8      |         200 |
|       8 | 0x007C      |         124 |
|       9 | 0x0013      |          19 |
|      10 | 0x0090      |         144 |
|      11 | 0x493C4     |      299972 |
|      12 | 0xFFF825D7  |  4294452695 |
|      13 | 0xFFFFF1EF  |  4294963695 |
|      14 | 0x03FA      |        1018 |
|      15 | 0x0005      |           5 |
|      16 | 0x1E72      |        7794 |
|      17 | 0x1E73      |        7795 |
|      18 | 0x1E74      |        7796 |
|      19 | 0x1E77      |        7799 |
|      20 | 0x1E75      |        7797 |

## String References

- **7742**: You dig up a strange wooden casket!

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

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 105 bytes |
| Instructions | 19        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 6E F0 FF  FF 7F 00 80 99 F0 FF FF     .Bn..........
0010: 7F 45 01 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 31  .E..........who1
0020: 02 80 1C 03 80 29 01 38  C2 07 01 02 1C 04 80 45  .....).8.......E
0030: 01 80 F0 FF FF 7F F0 FF  FF 7F 77 68 69 31 02 80  ..........whi1..
0040: 48 05 80 1C 03 80 6E F0  FF FF 7F 06 80 99 F0 FF  H.....n.........
0050: FF 7F 29 01 38 C2 07 01  03 1C 07 80 29 01 38 C2  ..).8.......).8.
0060: 07 01 04 A8 00 08 80 02  80 21 00                 .........!.     
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x6E] LocalPlayer uses emote 41*
  3: 0x000C [0x99] Wait for LocalPlayer animation to complete
  4: 0x0011 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0022 [0x1C] WAIT(60* ticks)
  6: 0x0025 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Casket (ID: 17285688/0x0107C238), tag_num=0x02)
  7: 0x002C [0x1C] WAIT(30* ticks)
  8: 0x002F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  9: 0x0040 [0x48] [System] [7742*]:
    → "You dig up a strange wooden casket!"
 10: 0x0043 [0x1C] WAIT(60* ticks)
 11: 0x0046 [0x6E] LocalPlayer uses emote 39*
 12: 0x004D [0x99] Wait for LocalPlayer animation to complete
 13: 0x0052 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Casket (ID: 17285688/0x0107C238), tag_num=0x03)
 14: 0x0059 [0x1C] WAIT(200* ticks)
 15: 0x005C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Casket (ID: 17285688/0x0107C238), tag_num=0x04)
 16: 0x0063 [0xA8] MAP_MARKER_CONTROL: Reset/unlock markers (no map display), zone=124*, marker=0*
 17: 0x0069 [0x21] END_EVENT
 18: 0x006A [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x006B    |
| Data Size    | 549 bytes |
| Instructions | 44        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   42 46 01 03 00             BF...
0070: 00 05 10 45 07 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
0080: 6F 30 02 80 55 07 80 F8  FF FF 7F F8 FF FF 7F 66  o0..U..........f
0090: 64 6F 30 4E 00 43 C2 07  01 4E 00 44 C2 07 01 38  do0N.C...N.D...8
00A0: 09 80 79 00 F0 FF FF 7F  43 C2 07 01 03 05 10 02  ..y.....C.......
00B0: 10 03 06 10 02 10 03 07  10 02 10 15 05 10 0A 80  ................
00C0: 15 06 10 03 80 3F 07 10  07 10 03 80 37 0B 80 0C  .....?......7...
00D0: 80 0D 80 0E 80 4A 43 C2  07 01 F0 FF FF 7F 45 0F  .....JC.......E.
00E0: 80 F8 FF FF 7F F8 FF FF  7F 73 31 30 34 02 80 45  .........s104..E
00F0: 07 80 F8 FF FF 7F F8 FF  FF 7F 66 64 69 31 02 80  ..........fdi1..
0100: 2B 43 C2 07 01 10 80 23  2B 43 C2 07 01 11 80 23  +C.....#+C.....#
0110: 02 04 10 02 80 01 53 01  03 05 10 04 10 03 06 10  ......S.........
0120: 04 10 03 07 10 04 10 15  05 10 0A 80 15 06 10 03  ................
0130: 80 3F 07 10 07 10 03 80  02 00 00 02 80 00 4B 01  .?............K.
0140: 2B 43 C2 07 01 12 80 23  01 53 01 2B 43 C2 07 01  +C.....#.S.+C...
0150: 13 80 23 52 0F 80 F8 FF  FF 7F F8 FF FF 7F 73 31  ..#R..........s1
0160: 30 34 45 07 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  04E..........fdo
0170: 31 02 80 55 07 80 F8 FF  FF 7F F8 FF FF 7F 66 64  1..U..........fd
0180: 6F 31 46 00 45 01 80 F0  FF FF 7F F0 FF FF 7F 71  o1F.E..........q
0190: 73 74 63 02 80 45 07 80  F8 FF FF 7F F8 FF FF 7F  stc..E..........
01A0: 66 64 69 32 02 80 21 00  4A 43 C2 07 01 F0 FF FF  fdi2..!.JC......
01B0: 7F 45 07 80 F8 FF FF 7F  F8 FF FF 7F 66 64 69 31  .E..........fdi1
01C0: 02 80 2B 43 C2 07 01 10  80 23 66 04 80 43 C2 07  ..+C.....#f..C..
01D0: 01 43 C2 07 01 74 6C 6B  30 2B 43 C2 07 01 11 80  .C...tlk0+C.....
01E0: 23 02 04 10 02 80 01 33  02 66 04 80 43 C2 07 01  #......3.f..C...
01F0: 43 C2 07 01 74 6C 6B 31  03 05 10 04 10 03 06 10  C...tlk1........
0200: 04 10 03 07 10 04 10 15  05 10 0A 80 15 06 10 03  ................
0210: 80 3F 07 10 07 10 03 80  02 00 00 02 80 00 2B 02  .?............+.
0220: 2B 43 C2 07 01 12 80 23  01 33 02 2B 43 C2 07 01  +C.....#.3.+C...
0230: 13 80 23 66 04 80 43 C2  07 01 43 C2 07 01 70 61  ..#f..C...C...pa
0240: 73 30 2B 43 C2 07 01 14  80 23 45 07 80 F8 FF FF  s0+C.....#E.....
0250: 7F F8 FF FF 7F 66 64 6F  31 02 80 55 07 80 F8 FF  .....fdo1..U....
0260: FF 7F F8 FF FF 7F 66 64  6F 31 46 00 45 01 80 F0  ......fdo1F.E...
0270: FF FF 7F F0 FF FF 7F 71  73 74 63 02 80 45 07 80  .......qstc..E..
0280: F8 FF FF 7F F8 FF FF 7F  66 64 69 32 02 80 21 00  ........fdi2..!.
```

#### Opcodes

```
  0: 0x006B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006C [0x46] CAMERA_CONTROL: Disable user control
  2: 0x006E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[5]
  3: 0x0073 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x0084 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
  5: 0x0093 [0x4E] SET_ENTITY_HIDE_FLAG: Show Kiteh Nanjyea (ID: 17285699/0x0107C243)
  6: 0x0099 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17285700/0x0107C244)
  7: 0x009F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x00A2 [0x79] LocalPlayer looks at Kiteh Nanjyea (ID: 17285699/0x0107C243) (Basic look)
  9: 0x00AC [0x03] Work_Zone[5] = Work_Zone[2]
 10: 0x00B1 [0x03] Work_Zone[6] = Work_Zone[2]
 11: 0x00B6 [0x03] Work_Zone[7] = Work_Zone[2]
 12: 0x00BB [0x15] Work_Zone[5] /= 144*
 13: 0x00C0 [0x15] Work_Zone[6] /= 60*
 14: 0x00C5 [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
 15: 0x00CC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=299.972*, z=-514.601*, y=-3.601*, direction=89.5°*
 16: 0x00D5 [0x4A] Kiteh Nanjyea (ID: 17285699/0x0107C243) looks at LocalPlayer
 17: 0x00DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s104" with entities [EventEntity, EventEntity], work=[5*, 0*]
 18: 0x00EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 19: 0x0100 [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7794*]:
    → "You've helped our poor girl find her way home! I don't know how to thank you!"
 20: 0x0107 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0108 [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7795*]:
    → "And to think you made it here in a mere $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
 22: 0x010F [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0110 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0153
 24: 0x0118 [0x03] Work_Zone[5] = Work_Zone[4]
 25: 0x011D [0x03] Work_Zone[6] = Work_Zone[4]
 26: 0x0122 [0x03] Work_Zone[7] = Work_Zone[4]
 27: 0x0127 [0x15] Work_Zone[5] /= 144*
 28: 0x012C [0x15] Work_Zone[6] /= 60*
 29: 0x0131 [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
 30: 0x0138 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x014B
 31: 0x0140 [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7796*]:
    → "Oh, and by the way, the fastest adventurer to date has been %0. That talented rider traversed the same course as you in $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
 32: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0148 [0x01] GOTO 0x0153
 34: 0x014B [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7799*]:
    → "Oh, and by the way, the fastest adventurer to date has been...you! Your remarkable record of $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time) still stands strong!"
 35: 0x0152 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0153:
 36: 0x0153 [0x52] END_LOAD_SCHEDULER: End scheduler "s104" with entities [EventEntity, EventEntity], work=5*
 37: 0x0162 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 38: 0x0173 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 39: 0x0182 [0x46] CAMERA_CONTROL: Restore default settings
 40: 0x0184 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 41: 0x0195 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 42: 0x01A6 [0x21] END_EVENT
 43: 0x01A7 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x01A8 [0x4A] Kiteh Nanjyea (ID: 17285699/0x0107C243) looks at LocalPlayer
     0x01B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x01C2 [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7794*]:
    → "You've helped our poor girl find her way home! I don't know how to thank you!"
     0x01C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01CA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Kiteh Nanjyea (ID: 17285699/0x0107C243), Kiteh Nanjyea (ID: 17285699/0x0107C243)], work=30*
     0x01D9 [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7795*]:
    → "And to think you made it here in a mere $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
     0x01E0 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01E1 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0233
     0x01E9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Kiteh Nanjyea (ID: 17285699/0x0107C243), Kiteh Nanjyea (ID: 17285699/0x0107C243)], work=30*
     0x01F8 [0x03] Work_Zone[5] = Work_Zone[4]
     0x01FD [0x03] Work_Zone[6] = Work_Zone[4]
     0x0202 [0x03] Work_Zone[7] = Work_Zone[4]
     0x0207 [0x15] Work_Zone[5] /= 144*
     0x020C [0x15] Work_Zone[6] /= 60*
     0x0211 [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
     0x0218 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x022B
     0x0220 [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7796*]:
    → "Oh, and by the way, the fastest adventurer to date has been %0. That talented rider traversed the same course as you in $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
     0x0227 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0228 [0x01] GOTO 0x0233
     0x022B [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7799*]:
    → "Oh, and by the way, the fastest adventurer to date has been...you! Your remarkable record of $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time) still stands strong!"
     0x0232 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0233 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [Kiteh Nanjyea (ID: 17285699/0x0107C243), Kiteh Nanjyea (ID: 17285699/0x0107C243)], work=30*
     0x0242 [0x2B] Kiteh Nanjyea (ID: 17285699/0x0107C243) [7797*]:
    → "Anyway, please take this as a token of our appreciation. And stop by again sometime. We may have more work for you!"
     0x0249 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x024A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x025B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
     0x026A [0x46] CAMERA_CONTROL: Restore default settings
     0x026C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x027D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x028E [0x21] END_EVENT
     0x028F [0x00] END_REQSTACK()
```
