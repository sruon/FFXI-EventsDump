# 17257077 - Cavernous Maw

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Tahrongi Canyon (ID: 117) |
| Block Size       | 324 bytes                 |
| Total Events     | 4                         |
| References Count | 11                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |    242 |             37 |
| [38](#event-38)       | 0x00F3       |      1 |              1 |
| [39](#event-39)       | 0x00F4       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CC7      |        7367 |
|       1 | 0x0003      |           3 |
|       2 | 0x1CC8      |        7368 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0x01C9      |         457 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0155      |         341 |

## String References

- **7367**: An unseen force is drawing you towards the maw.
- **7368**: Warp to Abyssea - [Dummy/La Theine/Konschtat/Tahrongi/Attohwa/Misareaux/Vunkerl/Altepa/Grauberg/Uleguerand]? [Proceed./Not yet.]

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

### Event 100

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 242 bytes |
| Instructions | 37        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 03  02 10 01 80 24 02 80 03    .H..#.....$...
0010: 80 04 80 25 02 00 10 04  80 00 E4 00 43 00 43 01  ...%........C.C.
0020: 03 00 00 03 10 02 00 00  03 80 00 35 00 03 01 10  ...........5....
0030: 03 80 01 38 00 01 EF 00  42 46 01 03 01 10 03 80  ...8....BF......
0040: 45 05 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 04  E..........fdo1.
0050: 80 1C 06 80 38 07 80 29  01 F0 FF FF 7F 02 45 08  ....8..)......E.
0060: 80 F0 FF FF 7F F0 FF FF  7F 61 62 30 36 04 80 45  .........ab06..E
0070: 05 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 04 80  ..........fdi1..
0080: 1C 06 80 45 05 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  ...E..........bl
0090: 6F 6E 04 80 45 09 80 F0  FF FF 7F F0 FF FF 7F 62  on..E..........b
00A0: 6C 6F 6E 04 80 45 05 80  F0 FF FF 7F F0 FF FF 7F  lon..E..........
00B0: 6F 76 6C 31 04 80 45 0A  80 F0 FF FF 7F F0 FF FF  ovl1..E.........
00C0: 7F 77 61 72 70 04 80 29  01 F0 FF FF 7F 03 45 05  .warp..)......E.
00D0: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 66 04 80 46  .........blof..F
00E0: 00 01 EF 00 02 00 10 03  80 00 EF 00 01 EF 00 20  ............... 
00F0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7367*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x03] Work_Zone[2] = 3*
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7368*, default_option=1*, option_flags=0*)
    → "Warp to Abyssea - [Dummy/La Theine/Konschtat/Tahrongi/Attohwa/Misareaux/Vunkerl/Altepa/Grauberg/Uleguerand]? [Proceed./Not yet.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00E4
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 10: 0x0025 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0035
 11: 0x002D [0x03] Work_Zone[1] = 1*
 12: 0x0032 [0x01] GOTO 0x0038
 13: 0x0035 [0x01] GOTO 0x00EF

SUBROUTINE_0038:
 14: 0x0038 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0039 [0x46] CAMERA_CONTROL: Disable user control
 16: 0x003B [0x03] Work_Zone[1] = 1*
 17: 0x0040 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0051 [0x1C] WAIT(60* ticks)
 19: 0x0054 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 20: 0x0057 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 21: 0x005E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ab06" with entities [LocalPlayer, LocalPlayer], work=[457*, 0*]
 22: 0x006F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0080 [0x1C] WAIT(60* ticks)
 24: 0x0083 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x0094 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 26: 0x00A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x00B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 28: 0x00C7 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 29: 0x00CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x00DF [0x46] CAMERA_CONTROL: Restore default settings
 31: 0x00E1 [0x01] GOTO 0x00EF
 32: 0x00E4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00EF
 33: 0x00EC [0x01] GOTO 0x00EF

SUBROUTINE_00EF:
 34: 0x00EF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 35: 0x00F1 [0x21] END_EVENT
 36: 0x00F2 [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          00                                          .            
```

#### Opcodes

```
  0: 0x00F3 [0x00] END_REQSTACK()
```

### Event 39

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             00                                        .           
```

#### Opcodes

```
  0: 0x00F4 [0x00] END_REQSTACK()
```
