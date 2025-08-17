# 17723648 - Explorer Moogle

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 696 bytes                     |
| Total Events     | 3                             |
| References Count | 27                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [863](#event-863)     | 0x0001       |     83 |             18 |
| [862](#event-862)     | 0x0054       |    476 |             93 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x012C      |         300 |
|       1 | 0x1F38      |        7992 |
|       2 | 0x0078      |         120 |
|       3 | 0x1F3D      |        7997 |
|       4 | 0x001E      |          30 |
|       5 | 0x1F39      |        7993 |
|       6 | 0x0000      |           0 |
|       7 | 0x0001      |           1 |
|       8 | 0x0002      |           2 |
|       9 | 0x0003      |           3 |
|      10 | 0x0004      |           4 |
|      11 | 0x0005      |           5 |
|      12 | 0x1F3A      |        7994 |
|      13 | 0x1F3B      |        7995 |
|      14 | 0x007A      |         122 |
|      15 | 0x0104      |         260 |
|      16 | 0x00C8      |         200 |
|      17 | 0x003C      |          60 |
|      18 | 0x1F3C      |        7996 |
|      19 | 0x00E7      |         231 |
|      20 | 0x00EA      |         234 |
|      21 | 0x00F0      |         240 |
|      22 | 0x0008      |           8 |
|      23 | 0x00F8      |         248 |
|      24 | 0x0010      |          16 |
|      25 | 0x00F9      |         249 |
|      26 | 0x0020      |          32 |

## String References

- **7992**: Greetings adventurer! I'm so glad you've come, kupo! To celebrate the safe recovery of all eleven of King Kupofried's mog tablets, we're offering a limited-time teleportation service for the low, low price of $0 gil! What do you say?
- **7993**: Teleport to where? (Cost: $0 gil.) [Nowhere./San d'Oria./Bastok./Windurst./Selbina./Mhaura.]
- **7994**: Your wish is my command, kupo! For a small fee of $0 gil, that is...
- **7995**: Safe travels, kupo!
- **7996**: Looks like you're light on funds, kupo... Sorry!
- **7997**: What's this? You're still new to this land? I'm afraid you're not yet strong enough to handle our potent moogle magic! Just forget I said anything, kupo!

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

### Event 863

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 83 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 6F  70 2C F8 FF FF 7F F8 FF   B.....op,......
0010: FF 7F 68 61 70 30 03 02  10 00 80 1D 01 80 23 2C  ..hap0........#,
0020: F8 FF FF 7F F8 FF FF 7F  67 61 6B 30 03 02 10 02  ........gak0....
0030: 80 27 10 01 71 0E 01 03  1D 03 80 23 2A 10 01 71  .'..q......#*..q
0040: 0E 01 2C F8 FF FF 7F F8  FF FF 7F 67 61 6B 31 1C  ..,........gak1.
0050: 04 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0009 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [EventEntity, EventEntity]
  5: 0x0016 [0x03] Work_Zone[2] = 300*
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7992*)
    → "Greetings adventurer! I'm so glad you've come, kupo! To celebrate the safe recovery of all eleven of King Kupofried's mog tablets, we're offering a limited-time teleportation service for the low, low price of $0 gil! What do you say?"
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak0" with entities [EventEntity, EventEntity]
  9: 0x002C [0x03] Work_Zone[2] = 120*
 10: 0x0031 [0x27] REQ_SET(priority=0x10, entity_id=mgtest (ID: 17723649/0x010E7101), tag_num=0x03)
 11: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=7997*)
    → "What's this? You're still new to this land? I'm afraid you're not yet strong enough to handle our potent moogle magic! Just forget I said anything, kupo!"
 12: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x003C [0x2A] GET_REQ_LEVEL(level=16, entity_id=mgtest (ID: 17723649/0x010E7101))
 14: 0x0042 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak1" with entities [EventEntity, EventEntity]
 15: 0x004F [0x1C] WAIT(30* ticks)
 16: 0x0052 [0x21] END_EVENT
 17: 0x0053 [0x00] END_REQSTACK()
```

### Event 862

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0054    |
| Data Size    | 476 bytes |
| Instructions | 57        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             42 1E F0 FF  FF 7F 6F 70 03 00 00 02      B.....op....
0060: 10 03 01 00 04 10 1A DF  01 2C F8 FF FF 7F F8 FF  .........,......
0070: FF 7F 68 61 70 30 03 02  10 00 80 1D 01 80 23 2C  ..hap0........#,
0080: F8 FF FF 7F F8 FF FF 7F  68 61 70 31 24 05 80 06  ........hap1$...
0090: 80 02 00 25 02 00 10 06  80 00 A1 00 21 00 01 46  ...%........!..F
00A0: 01 02 00 10 07 80 00 C2  00 02 01 00 06 80 00 BC  ................
00B0: 00 03 01 10 07 80 01 46  01 01 BF 00 01 AA 01 01  .......F........
00C0: 46 01 02 00 10 08 80 00  E3 00 02 01 00 06 80 00  F...............
00D0: DD 00 03 01 10 08 80 01  46 01 01 E0 00 01 AA 01  ........F.......
00E0: 01 46 01 02 00 10 09 80  00 04 01 02 01 00 06 80  .F..............
00F0: 00 FE 00 03 01 10 09 80  01 46 01 01 01 01 01 AA  .........F......
0100: 01 01 46 01 02 00 10 0A  80 00 25 01 02 01 00 06  ..F.......%.....
0110: 80 00 1F 01 03 01 10 0A  80 01 46 01 01 22 01 01  ..........F.."..
0120: AA 01 01 46 01 02 00 10  0B 80 00 46 01 02 01 00  ...F.......F....
0130: 06 80 00 40 01 03 01 10  0B 80 01 46 01 01 43 01  ...@.......F..C.
0140: 01 AA 01 01 46 01 2C F8  FF FF 7F F8 FF FF 7F 68  ....F.,........h
0150: 61 70 30 03 02 10 00 80  1D 0C 80 23 2C F8 FF FF  ap0........#,...
0160: 7F F8 FF FF 7F 68 61 70  31 53 F8 FF FF 7F F8 FF  .....hap1S......
0170: FF 7F 68 61 70 31 2C F8  FF FF 7F F8 FF FF 7F 6A  ..hap1,........j
0180: 6F 62 30 1D 0D 80 73 0E  80 01 71 0E 01 F0 FF FF  ob0...s...q.....
0190: 7F 1C 0F 80 45 10 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
01A0: 64 6F 31 06 80 1C 11 80  21 00 2C F8 FF FF 7F F8  do1.....!.,.....
01B0: FF FF 7F 67 61 6B 30 03  02 10 02 80 27 10 01 71  ...gak0.....'..q
01C0: 0E 01 03 1D 12 80 23 2A  10 01 71 0E 01 2C F8 FF  ......#*..q..,..
01D0: FF 7F F8 FF FF 7F 67 61  6B 31 1C 04 80 21 00 02  ......gak1...!..
01E0: 00 00 13 80 80 EF 01 03  02 00 08 80 01 2F 02 02  ............./..
01F0: 00 00 14 80 80 FF 01 03  02 00 0A 80 01 2F 02 02  ............./..
0200: 00 00 15 80 80 0F 02 03  02 00 16 80 01 2F 02 02  ............./..
0210: 00 00 17 80 80 1F 02 03  02 00 18 80 01 2F 02 02  ............./..
0220: 00 00 19 80 80 2F 02 03  02 00 1A 80 01 2F 02 1B  ...../......./..
```

#### Opcodes

```
  0: 0x0054 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0055 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x005A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x005B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x005C [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  5: 0x0061 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[4]
  6: 0x0066 [0x1A] CALL_SUBROUTINE(address=0x01DF)
  7: 0x0069 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [EventEntity, EventEntity]
  8: 0x0076 [0x03] Work_Zone[2] = 300*
  9: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=7992*)
    → "Greetings adventurer! I'm so glad you've come, kupo! To celebrate the safe recovery of all eleven of King Kupofried's mog tablets, we're offering a limited-time teleportation service for the low, low price of $0 gil! What do you say?"
 10: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x007F [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap1" with entities [EventEntity, EventEntity]
 12: 0x008C [0x24] CREATE_DIALOG(message_id=7993*, default_option=0*, option_flags=ExtData[1]->WorkLocal[2])
    → "Teleport to where? (Cost: $0 gil.) [Nowhere./San d'Oria./Bastok./Windurst./Selbina./Mhaura.]"
 13: 0x0093 [0x25] WAIT_DIALOG_SELECT()
 14: 0x0094 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00A1
 15: 0x009C [0x21] END_EVENT
 16: 0x009D [0x00] END_REQSTACK()

SUBROUTINE_0146:
 17: 0x0146 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [EventEntity, EventEntity]
 18: 0x0153 [0x03] Work_Zone[2] = 300*
 19: 0x0158 [0x1D] PRINT_EVENT_MESSAGE(message_id=7994*)
    → "Your wish is my command, kupo! For a small fee of $0 gil, that is..."
 20: 0x015B [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x015C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap1" with entities [EventEntity, EventEntity]
 22: 0x0169 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap1" with entities [EventEntity, EventEntity]
 23: 0x0176 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "job0" with entities [EventEntity, EventEntity]
 24: 0x0183 [0x1D] PRINT_EVENT_MESSAGE(message_id=7995*)
    → "Safe travels, kupo!"
 25: 0x0186 [0x73] mgtest (ID: 17723649/0x010E7101) casts magic 122* on LocalPlayer
 26: 0x0191 [0x1C] WAIT(260* ticks)
 27: 0x0194 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x01A5 [0x1C] WAIT(60* ticks)
 29: 0x01A8 [0x21] END_EVENT
 30: 0x01A9 [0x00] END_REQSTACK()

SUBROUTINE_01AA:
 31: 0x01AA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak0" with entities [EventEntity, EventEntity]
 32: 0x01B7 [0x03] Work_Zone[2] = 120*
 33: 0x01BC [0x27] REQ_SET(priority=0x10, entity_id=mgtest (ID: 17723649/0x010E7101), tag_num=0x03)
 34: 0x01C3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7996*)
    → "Looks like you're light on funds, kupo... Sorry!"
 35: 0x01C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x01C7 [0x2A] GET_REQ_LEVEL(level=16, entity_id=mgtest (ID: 17723649/0x010E7101))
 37: 0x01CD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak1" with entities [EventEntity, EventEntity]
 38: 0x01DA [0x1C] WAIT(30* ticks)
 39: 0x01DD [0x21] END_EVENT
 40: 0x01DE [0x00] END_REQSTACK()

SUBROUTINE_01DF:
 41: 0x01DF [0x02] IF !(ExtData[1]->WorkLocal[0] == 231*) GOTO 0x01EF
 42: 0x01E7 [0x03] ExtData[1]->WorkLocal[2] = 2*
 43: 0x01EC [0x01] GOTO 0x022F
 44: 0x01EF [0x02] IF !(ExtData[1]->WorkLocal[0] == 234*) GOTO 0x01FF
 45: 0x01F7 [0x03] ExtData[1]->WorkLocal[2] = 4*
 46: 0x01FC [0x01] GOTO 0x022F
 47: 0x01FF [0x02] IF !(ExtData[1]->WorkLocal[0] == 240*) GOTO 0x020F
 48: 0x0207 [0x03] ExtData[1]->WorkLocal[2] = 8*
 49: 0x020C [0x01] GOTO 0x022F
 50: 0x020F [0x02] IF !(ExtData[1]->WorkLocal[0] == 248*) GOTO 0x021F
 51: 0x0217 [0x03] ExtData[1]->WorkLocal[2] = 16*
 52: 0x021C [0x01] GOTO 0x022F
 53: 0x021F [0x02] IF !(ExtData[1]->WorkLocal[0] == 249*) GOTO 0x022F
 54: 0x0227 [0x03] ExtData[1]->WorkLocal[2] = 32*
 55: 0x022C [0x01] GOTO 0x022F

SUBROUTINE_022F:
 56: 0x022F [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x009E [0x01] GOTO 0x0146
     0x00B9 [0x01] GOTO 0x00BF
     0x00BF [0x01] GOTO 0x0146
     0x00DA [0x01] GOTO 0x00E0
     0x00E0 [0x01] GOTO 0x0146
     0x00FB [0x01] GOTO 0x0101
     0x0101 [0x01] GOTO 0x0146
     0x011C [0x01] GOTO 0x0122
     0x0122 [0x01] GOTO 0x0146
     0x013D [0x01] GOTO 0x0143
     0x0143 [0x01] GOTO 0x0146
```
