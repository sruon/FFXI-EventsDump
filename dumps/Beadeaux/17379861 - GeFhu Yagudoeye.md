# 17379861 - GeFhu Yagudoeye

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Beadeaux (ID: 147) |
| Block Size       | 492 bytes          |
| Total Events     | 6                  |
| References Count | 12                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     14 |              2 |
| [65535.3](#event-655353) | 0x001F       |     16 |              2 |
| [65535.4](#event-655354) | 0x002F       |     14 |              2 |
| [124](#event-124)        | 0x003D       |    342 |             52 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00E3      |         227 |
|       1 | 0x1E5F      |        7775 |
|       2 | 0x1E63      |        7779 |
|       3 | 0x001E      |          30 |
|       4 | 0x0003      |           3 |
|       5 | 0x0016      |          22 |
|       6 | 0x0000      |           0 |
|       7 | 0x00C8      |         200 |
|       8 | 0x0013      |          19 |
|       9 | 0x1E64      |        7780 |
|      10 | 0x012C      |         300 |
|      11 | 0x0078      |         120 |

## String References

- **7775**: Hu-urr...!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=227*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=227*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 124

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x003D    |
| Data Size    | 342 bytes |
| Instructions | 52        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         20 01 42                .B
0040: 46 01 29 0B 16 32 09 01  02 92 01 17 32 09 01 92  F.)..2......2...
0050: 01 18 32 09 01 92 01 19  32 09 01 92 01 1A 32 09  ..2.....2.....2.
0060: 01 92 01 1B 32 09 01 29  08 15 32 09 01 01 1D 01  ....2..)..2.....
0070: 80 23 29 08 15 32 09 01  02 4A F0 FF FF 7F 16 32  .#)..2...J.....2
0080: 09 01 2B 16 32 09 01 02  80 23 27 0B EB 31 09 01  ..+.2....#'..1..
0090: 02 4E 00 16 32 09 01 4E  00 17 32 09 01 4E 00 18  .N..2..N..2..N..
00A0: 32 09 01 4E 00 19 32 09  01 4E 00 1A 32 09 01 4E  2..N..2..N..2..N
00B0: 00 1B 32 09 01 80 16 32  09 01 27 0B 16 32 09 01  ..2....2..'..2..
00C0: 03 27 0B 17 32 09 01 02  27 0B 18 32 09 01 02 27  .'..2...'..2...'
00D0: 0B 19 32 09 01 02 27 0B  1A 32 09 01 02 27 0B 1B  ..2...'..2...'..
00E0: 32 09 01 02 1C 03 80 38  04 80 45 05 80 F8 FF FF  2......8..E.....
00F0: 7F F8 FF FF 7F 73 30 33  36 06 80 45 07 80 F8 FF  .....s036..E....
0100: FF 7F F8 FF FF 7F 66 64  69 31 06 80 1C 07 80 52  ......fdi1.....R
0110: 05 80 F8 FF FF 7F F8 FF  FF 7F 73 30 33 36 38 08  ..........s0368.
0120: 80 45 07 80 F0 FF FF 7F  F0 FF FF 7F 6F 76 6C 31  .E..........ovl1
0130: 06 80 45 05 80 F8 FF FF  7F F8 FF FF 7F 73 30 33  ..E..........s03
0140: 37 06 80 2B 16 32 09 01  09 80 23 1C 0A 80 45 07  7..+.2....#...E.
0150: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 06 80 1C  .........fdo1...
0160: 0B 80 52 05 80 F8 FF FF  7F F8 FF FF 7F 73 30 33  ..R..........s03
0170: 37 4E 00 F0 FF FF 7F 80  F0 FF FF 7F 46 00 45 07  7N..........F.E.
0180: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 06 80 20  .........fdi1.. 
0190: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x003D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x003F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0040 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0042 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zeelozok (ID: 17379862/0x01093216), tag_num=0x02)
  4: 0x0049 [0x92] ??? (ID: 17379863/0x01093217)->Render.Flags3 ^= 0x01
  5: 0x004F [0x92] ??? (ID: 17379864/0x01093218)->Render.Flags3 ^= 0x01
  6: 0x0055 [0x92] ??? (ID: 17379865/0x01093219)->Render.Flags3 ^= 0x01
  7: 0x005B [0x92] ??? (ID: 17379866/0x0109321A)->Render.Flags3 ^= 0x01
  8: 0x0061 [0x92] ??? (ID: 17379867/0x0109321B)->Render.Flags3 ^= 0x01
  9: 0x0067 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ge'Fhu Yagudoeye (ID: 17379861/0x01093215), tag_num=0x01)
 10: 0x006E [0x1D] PRINT_EVENT_MESSAGE(message_id=7775*)
    → "Hu-urr...!"
 11: 0x0071 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0072 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ge'Fhu Yagudoeye (ID: 17379861/0x01093215), tag_num=0x02)
 13: 0x0079 [0x4A] LocalPlayer looks at Zeelozok (ID: 17379862/0x01093216)
 14: 0x0082 [0x2B] Zeelozok (ID: 17379862/0x01093216) [7779*]:
    → "Quadav betrayers!"
 15: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x008A [0x27] REQ_SET(priority=0x0B, entity_id=Sliding Door (ID: 17379819/0x010931EB), tag_num=0x02)
 17: 0x0091 [0x4E] SET_ENTITY_HIDE_FLAG: Show Zeelozok (ID: 17379862/0x01093216)
 18: 0x0097 [0x4E] SET_ENTITY_HIDE_FLAG: Show ??? (ID: 17379863/0x01093217)
 19: 0x009D [0x4E] SET_ENTITY_HIDE_FLAG: Show ??? (ID: 17379864/0x01093218)
 20: 0x00A3 [0x4E] SET_ENTITY_HIDE_FLAG: Show ??? (ID: 17379865/0x01093219)
 21: 0x00A9 [0x4E] SET_ENTITY_HIDE_FLAG: Show ??? (ID: 17379866/0x0109321A)
 22: 0x00AF [0x4E] SET_ENTITY_HIDE_FLAG: Show ??? (ID: 17379867/0x0109321B)
 23: 0x00B5 [0x80] LOAD_WAIT(entity=Zeelozok (ID: 17379862/0x01093216))
 24: 0x00BA [0x27] REQ_SET(priority=0x0B, entity_id=Zeelozok (ID: 17379862/0x01093216), tag_num=0x03)
 25: 0x00C1 [0x27] REQ_SET(priority=0x0B, entity_id=??? (ID: 17379863/0x01093217), tag_num=0x02)
 26: 0x00C8 [0x27] REQ_SET(priority=0x0B, entity_id=??? (ID: 17379864/0x01093218), tag_num=0x02)
 27: 0x00CF [0x27] REQ_SET(priority=0x0B, entity_id=??? (ID: 17379865/0x01093219), tag_num=0x02)
 28: 0x00D6 [0x27] REQ_SET(priority=0x0B, entity_id=??? (ID: 17379866/0x0109321A), tag_num=0x02)
 29: 0x00DD [0x27] REQ_SET(priority=0x0B, entity_id=??? (ID: 17379867/0x0109321B), tag_num=0x02)
 30: 0x00E4 [0x1C] WAIT(30* ticks)
 31: 0x00E7 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 32: 0x00EA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s036" with entities [EventEntity, EventEntity], work=[22*, 0*]
 33: 0x00FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 34: 0x010C [0x1C] WAIT(200* ticks)
 35: 0x010F [0x52] END_LOAD_SCHEDULER: End scheduler "s036" with entities [EventEntity, EventEntity], work=22*
 36: 0x011E [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 37: 0x0121 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x0132 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s037" with entities [EventEntity, EventEntity], work=[22*, 0*]
 39: 0x0143 [0x2B] Zeelozok (ID: 17379862/0x01093216) [7780*]:
    → "Promathia! Save your servant!"
 40: 0x014A [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x014B [0x1C] WAIT(300* ticks)
 42: 0x014E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x015F [0x1C] WAIT(120* ticks)
 44: 0x0162 [0x52] END_LOAD_SCHEDULER: End scheduler "s037" with entities [EventEntity, EventEntity], work=22*
 45: 0x0171 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 46: 0x0177 [0x80] LOAD_WAIT(entity=LocalPlayer)
 47: 0x017C [0x46] CAMERA_CONTROL: Restore default settings
 48: 0x017E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 49: 0x018F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 50: 0x0191 [0x21] END_EVENT
 51: 0x0192 [0x00] END_REQSTACK()
```
