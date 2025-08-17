# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ordelle's Caves (ID: 193) |
| Block Size       | 904 bytes                 |
| Total Events     | 6                         |
| References Count | 39                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |    185 |             37 |
| [10](#event-10)          | 0x00E0       |    471 |             62 |
| [65535.3](#event-655353) | 0x02B7       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x000A      |          10 |
|       4 | 0x0009      |           9 |
|       5 | 0x0046      |          70 |
|       6 | 0x008C      |         140 |
|       7 | 0x00D2      |         210 |
|       8 | 0x028E      |         654 |
|       9 | 0xFFFEF84A  |  4294899786 |
|      10 | 0xA2732     |      665394 |
|      11 | 0x01F3      |         499 |
|      12 | 0x0680      |        1664 |
|      13 | 0x00C8      |         200 |
|      14 | 0x0000      |           0 |
|      15 | 0x00CC      |         204 |
|      16 | 0x000D      |          13 |
|      17 | 0xFFFEEB66  |  4294896486 |
|      18 | 0xA1AD0     |      662224 |
|      19 | 0x0014      |          20 |
|      20 | 0x1CFB      |        7419 |
|      21 | 0x1CFC      |        7420 |
|      22 | 0x001E      |          30 |
|      23 | 0x1CFD      |        7421 |
|      24 | 0x1CFE      |        7422 |
|      25 | 0x0178      |         376 |
|      26 | 0x1CFF      |        7423 |
|      27 | 0x1D00      |        7424 |
|      28 | 0x1D01      |        7425 |
|      29 | 0x1D02      |        7426 |
|      30 | 0x1D03      |        7427 |
|      31 | 0x1D04      |        7428 |
|      32 | 0x1D05      |        7429 |
|      33 | 0x0D21      |        3361 |
|      34 | 0x1D06      |        7430 |
|      35 | 0xFFFEA89D  |  4294879389 |
|      36 | 0x2FF5A     |      196442 |
|      37 | 0x7D5F      |       32095 |
|      38 | 0x0783      |        1923 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 07 7F 1A  4C 00 66 01 00 F8 FF FF    ......L.f.....
0010: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
0020: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0019 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0027    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      03  00 00 07 7F 1A 4C 00 66         ......L.f
0030: 01 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
0040: FF FF 7F F8 FF FF 7F 73  68 61 31 00 03 01 00 00  .......sha1.....
0050: 00 02 01 00 00 80 05 61  00 08 01 00 01 80 01 66  .......a.......f
0060: 00 08 01 00 02 80 14 01  00 03 80 07 01 00 04 80  ................
0070: 1B 03 01 00 00 00 02 01  00 00 80 05 86 00 08 01  ................
0080: 00 01 80 01 8B 00 08 01  00 02 80 14 01 00 03 80  ................
0090: 07 01 00 05 80 1B 03 01  00 00 00 02 01 00 00 80  ................
00A0: 05 AB 00 08 01 00 01 80  01 B0 00 08 01 00 02 80  ................
00B0: 14 01 00 03 80 07 01 00  06 80 1B 03 01 00 00 00  ................
00C0: 02 01 00 00 80 05 D0 00  08 01 00 01 80 01 D5 00  ................
00D0: 08 01 00 02 80 14 01 00  03 80 07 01 00 07 80 1B  ................
```

#### Opcodes

```
  0: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x002C [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x004B [0x00] END_REQSTACK()

SUBROUTINE_004C:
  5: 0x004C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  6: 0x0051 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0061
  7: 0x0059 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  8: 0x005E [0x01] GOTO 0x0066
  9: 0x0061 [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0066:
 10: 0x0066 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 11: 0x006B [0x07] ExtData[1]->WorkLocal[1] += 9*
 12: 0x0070 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0071 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0076 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0086
     0x007E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0083 [0x01] GOTO 0x008B
     0x0086 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x008B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0090 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0095 [0x1B] RETURN
     0x0096 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x009B [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00AB
     0x00A3 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00A8 [0x01] GOTO 0x00B0
     0x00AB [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00B0 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00B5 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00BA [0x1B] RETURN
     0x00BB [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00C0 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00D0
     0x00C8 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00CD [0x01] GOTO 0x00D5
     0x00D0 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00D5 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00DA [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x00DF [0x1B] RETURN
```

### Event 10

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E0    |
| Data Size    | 471 bytes |
| Instructions | 62        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 22 00 03 09 10 08 80 46  01 42 37 09 80 0A 80 0B  "......F.B7.....
00F0: 80 0C 80 45 0D 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
0100: 69 32 0E 80 45 0F 80 F8  FF FF 7F F8 FF FF 7F 73  i2..E..........s
0110: 30 31 32 0E 80 32 10 80  1F 00 11 80 12 80 0B 80  012..2..........
0120: 1F 01 1C 13 80 79 00 B4  11 0C 01 F0 FF FF 7F 27  .....y.........'
0130: 0A B4 11 0C 01 02 2B B4  11 0C 01 14 80 23 2B B4  ......+......#+.
0140: 11 0C 01 15 80 23 1E B4  11 0C 01 1C 16 80 52 0F  .....#........R.
0150: 80 F8 FF FF 7F F8 FF FF  7F 73 30 31 32 45 0F 80  .........s012E..
0160: F8 FF FF 7F F8 FF FF 7F  73 30 31 33 0E 80 2B B4  ........s013..+.
0170: 11 0C 01 17 80 23 2B B4  11 0C 01 18 80 23 2A 0A  .....#+......#*.
0180: B4 11 0C 01 5B 19 80 B4  11 0C 01 B4 11 0C 01 74  ....[..........t
0190: 6C 6B 30 2B B4 11 0C 01  1A 80 23 2B B4 11 0C 01  lk0+......#+....
01A0: 1B 80 23 6B 69 64 6C 30  B4 11 0C 01 2B B4 11 0C  ..#kidl0....+...
01B0: 01 1C 80 23 45 0D 80 F8  FF FF 7F F8 FF FF 7F 66  ...#E..........f
01C0: 64 6F 30 0E 80 55 0D 80  F8 FF FF 7F F8 FF FF 7F  do0..U..........
01D0: 66 64 6F 30 52 0F 80 F8  FF FF 7F F8 FF FF 7F 73  fdo0R..........s
01E0: 30 31 33 45 0F 80 F8 FF  FF 7F F8 FF FF 7F 73 30  013E..........s0
01F0: 31 34 0E 80 45 0D 80 F8  FF FF 7F F8 FF FF 7F 66  14..E..........f
0200: 64 69 31 0E 80 2B B4 11  0C 01 1D 80 23 5B 19 80  di1..+......#[..
0210: B4 11 0C 01 B4 11 0C 01  74 6C 6B 30 2B B4 11 0C  ........tlk0+...
0220: 01 1E 80 23 2B B4 11 0C  01 1F 80 23 6B 69 64 6C  ...#+......#kidl
0230: 30 B4 11 0C 01 2B B4 11  0C 01 20 80 23 52 0F 80  0....+.... .#R..
0240: F8 FF FF 7F F8 FF FF 7F  73 30 31 34 45 0F 80 F8  ........s014E...
0250: FF FF 7F F8 FF FF 7F 73  30 31 35 0E 80 4B B4 11  .......s015..K..
0260: 0C 01 21 80 2B B4 11 0C  01 22 80 23 27 0A B4 11  ..!.+....".#'...
0270: 0C 01 03 45 0D 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
0280: 6F 32 0E 80 55 0D 80 F8  FF FF 7F F8 FF FF 7F 66  o2..U..........f
0290: 64 6F 32 52 0F 80 F8 FF  FF 7F F8 FF FF 7F 73 30  do2R..........s0
02A0: 31 35 46 00 45 0D 80 F8  FF FF 7F F8 FF FF 7F 66  15F.E..........f
02B0: 64 69 32 0E 80 21 00                              di2..!.         
```

#### Opcodes

```
  0: 0x00E0 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00E2 [0x03] Work_Zone[9] = 654*
  2: 0x00E7 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x00E9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x00EA [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-67.510*, z=665.394*, y=0.499*, direction=146.2°*
  5: 0x00F3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
  6: 0x0104 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s012" with entities [EventEntity, EventEntity], work=[204*, 0*]
  7: 0x0115 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  8: 0x0118 [0x1F] MOVE_ENTITY: EventEntity moves to X=-70.810*, Z=662.224*, Y=0.499*
  9: 0x0120 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x0122 [0x1C] WAIT(20* ticks)
 11: 0x0125 [0x79] Zeid (ID: 17568180/0x010C11B4) looks at LocalPlayer (Basic look)
 12: 0x012F [0x27] REQ_SET(priority=0x0A, entity_id=Zeid (ID: 17568180/0x010C11B4), tag_num=0x02)
 13: 0x0136 [0x2B] Zeid (ID: 17568180/0x010C11B4) [7419*]:
    → "Evil weapons...this is what we call weapons that have gained a will of their own after being exposed to some kind of powerful energy."
 14: 0x013D [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x013E [0x2B] Zeid (ID: 17568180/0x010C11B4) [7420*]:
    → "Ever do they seek to taste new blood. They enslave kobolds--earth spirits with telekinetic powers--and force them to do their bidding."
 16: 0x0145 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0146 [0x1E] EventEntity looks at Zeid (ID: 17568180/0x010C11B4) and starts talking
 18: 0x014B [0x1C] WAIT(30* ticks)
 19: 0x014E [0x52] END_LOAD_SCHEDULER: End scheduler "s012" with entities [EventEntity, EventEntity], work=204*
 20: 0x015D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s013" with entities [EventEntity, EventEntity], work=[204*, 0*]
 21: 0x016E [0x2B] Zeid (ID: 17568180/0x010C11B4) [7421*]:
    → "I had a feeling you would come, ever since I wrote that letter to Cid. Well? Does your blade shine with darkness?"
 22: 0x0175 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0176 [0x2B] Zeid (ID: 17568180/0x010C11B4) [7422*]:
    → "At any rate, that is the theory of the evil weapons' origin. By "powerful energy," most scholars suspect the Crystal Lines."
 24: 0x017D [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x017E [0x2A] GET_REQ_LEVEL(level=10, entity_id=Zeid (ID: 17568180/0x010C11B4))
 26: 0x0184 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Zeid (ID: 17568180/0x010C11B4), Zeid (ID: 17568180/0x010C11B4)], work=376*
 27: 0x0193 [0x2B] Zeid (ID: 17568180/0x010C11B4) [7423*]:
    → "Even though the Crag of Holla is close, Ordelle's Caves are not under the influence of the Crystal Line that emanates from that place. So strange that an evil weapon would appear here..."
 28: 0x019A [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x019B [0x2B] Zeid (ID: 17568180/0x010C11B4) [7424*]:
    → "The adventurer that happened upon the evil weapon said he was carrying $7 for crafting."
 30: 0x01A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x01A3 [0x6B] STOP_AND_IDLE: Zeid (ID: 17568180/0x010C11B4) stops current action and resets to idle (animation="idl0")
 32: 0x01AC [0x2B] Zeid (ID: 17568180/0x010C11B4) [7425*]:
    → "The evil weapon appeared right when he accidentally dropped $7. Just like my armor, the weapon bore the signature of Gerwitz."
 33: 0x01B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x01B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 35: 0x01C5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
 36: 0x01D4 [0x52] END_LOAD_SCHEDULER: End scheduler "s013" with entities [EventEntity, EventEntity], work=204*
 37: 0x01E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s014" with entities [EventEntity, EventEntity], work=[204*, 0*]
 38: 0x01F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 39: 0x0205 [0x2B] Zeid (ID: 17568180/0x010C11B4) [7426*]:
    → "Gerwitz is a Galkan blacksmith who had left for his journey of rebirth over thirty years ago. Normally, he would be spinning new memories someplace out there."
 40: 0x020C [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x020D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Zeid (ID: 17568180/0x010C11B4), Zeid (ID: 17568180/0x010C11B4)], work=376*
 42: 0x021C [0x2B] Zeid (ID: 17568180/0x010C11B4) [7427*]:
    → "But he desired something. And now he seeks it in this place, ever refusing to be reborn."
 43: 0x0223 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x0224 [0x2B] Zeid (ID: 17568180/0x010C11B4) [7428*]:
    → "I doubt what he seeks is me. I combed every corner of this land, yet no trace of him could I find."
 45: 0x022B [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x022C [0x6B] STOP_AND_IDLE: Zeid (ID: 17568180/0x010C11B4) stops current action and resets to idle (animation="idl0")
 47: 0x0235 [0x2B] Zeid (ID: 17568180/0x010C11B4) [7429*]:
    → "He wants something from a person with newfound strength. Perhaps he wants the blood of someone with power and a future. Or perhaps..."
 48: 0x023C [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x023D [0x52] END_LOAD_SCHEDULER: End scheduler "s014" with entities [EventEntity, EventEntity], work=204*
 50: 0x024C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s015" with entities [EventEntity, EventEntity], work=[204*, 0*]
 51: 0x025D [0x4B] UPDATE_ENTITY_YAW(entity=Zeid (ID: 17568180/0x010C11B4), yaw=18.5°*)
 52: 0x0264 [0x2B] Zeid (ID: 17568180/0x010C11B4) [7430*]:
    → "I believe he must have called you here. Whether you will answer his call is up to you and your blade..."
 53: 0x026B [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x026C [0x27] REQ_SET(priority=0x0A, entity_id=Zeid (ID: 17568180/0x010C11B4), tag_num=0x03)
 55: 0x0273 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 56: 0x0284 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [EventEntity, EventEntity], work=200*
 57: 0x0293 [0x52] END_LOAD_SCHEDULER: End scheduler "s015" with entities [EventEntity, EventEntity], work=204*
 58: 0x02A2 [0x46] CAMERA_CONTROL: Restore default settings
 59: 0x02A4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 60: 0x02B5 [0x21] END_EVENT
 61: 0x02B6 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02B7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                      37  23 80 24 80 25 80 26 80         7#.$.%.&.
02C0: 00                                                .               
```

#### Opcodes

```
  0: 0x02B7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-87.907*, z=196.442*, y=32.095*, direction=169.0°*
  1: 0x02C0 [0x00] END_REQSTACK()
```
