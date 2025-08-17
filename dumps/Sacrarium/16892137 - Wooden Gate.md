# 16892137 - Wooden Gate

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Sacrarium (ID: 28) |
| Block Size       | 276 bytes          |
| Total Events     | 5                  |
| References Count | 10                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [5](#event-5)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      2 |              2 |
| [65535.2](#event-655352) | 0x0004       |      2 |              2 |
| [110](#event-110)        | 0x0006       |    194 |             34 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0246      |         582 |
|       1 | 0x1C40      |        7232 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x00C8      |         200 |
|       5 | 0x003C      |          60 |
|       6 | 0x0012      |          18 |
|       7 | 0x00A0      |         160 |
|       8 | 0x0096      |         150 |
|       9 | 0x00B4      |         180 |

## String References

- **7232**: Use the $3? [Yes./No.]

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

### Event 5

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4C 00                                         L.            
```

#### Opcodes

```
  0: 0x0002 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             4D 00                                     M.          
```

#### Opcodes

```
  0: 0x0004 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0006    |
| Data Size    | 194 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   20 01  03 02 10 00 80 24 01 80         ......$..
0010: 02 80 03 80 25 02 00 10  03 80 00 B9 00 43 00 43  ....%........C.C
0020: 01 46 01 42 45 04 80 F0  FF FF 7F F0 FF FF 7F 66  .F.BE..........f
0030: 64 6F 31 03 80 1C 05 80  38 06 80 45 07 80 F0 FF  do1.....8..E....
0040: FF 7F F0 FF FF 7F 32 38  65 6E 03 80 29 01 F0 FF  ......28en..)...
0050: FF 7F 18 29 01 F0 FF FF  7F 19 45 04 80 F0 FF FF  ...)......E.....
0060: 7F F0 FF FF 7F 66 64 69  31 03 80 1C 05 80 4C 1C  .....fdi1.....L.
0070: 08 80 27 01 F0 FF FF 7F  1A 1C 09 80 4D 1C 08 80  ..'.........M...
0080: 45 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 03  E..........fdo1.
0090: 80 1C 05 80 52 07 80 F0  FF FF 7F F0 FF FF 7F 32  ....R..........2
00A0: 38 65 6E 45 04 80 F0 FF  FF 7F F0 FF FF 7F 66 64  8enE..........fd
00B0: 69 31 03 80 46 00 01 C4  00 02 00 10 02 80 00 C4  i1..F...........
00C0: 00 01 C4 00 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0006 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0008 [0x03] Work_Zone[2] = 582*
  2: 0x000D [0x24] CREATE_DIALOG(message_id=7232*, default_option=1*, option_flags=0*)
    → "Use the $3? [Yes./No.]"
  3: 0x0014 [0x25] WAIT_DIALOG_SELECT()
  4: 0x0015 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00B9
  5: 0x001D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x001F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0021 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0023 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0024 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0035 [0x1C] WAIT(60* ticks)
 11: 0x0038 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 12: 0x003B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "28en" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 13: 0x004C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x18)
 14: 0x0053 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x19)
 15: 0x005A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x006B [0x1C] WAIT(60* ticks)
 17: 0x006E [0x4C] EventEntity->StatusEvent = 8 // Open door
 18: 0x006F [0x1C] WAIT(150* ticks)
 19: 0x0072 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x1A)
 20: 0x0079 [0x1C] WAIT(180* ticks)
 21: 0x007C [0x4D] EventEntity->StatusEvent = 9 // Close door
 22: 0x007D [0x1C] WAIT(150* ticks)
 23: 0x0080 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x0091 [0x1C] WAIT(60* ticks)
 25: 0x0094 [0x52] END_LOAD_SCHEDULER: End scheduler "28en" with entities [LocalPlayer, LocalPlayer], work=160*
 26: 0x00A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x00B4 [0x46] CAMERA_CONTROL: Restore default settings
 28: 0x00B6 [0x01] GOTO 0x00C4
 29: 0x00B9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00C4
 30: 0x00C1 [0x01] GOTO 0x00C4

SUBROUTINE_00C4:
 31: 0x00C4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 32: 0x00C6 [0x21] END_EVENT
 33: 0x00C7 [0x00] END_REQSTACK()
```
