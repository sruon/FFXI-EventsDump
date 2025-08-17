# 16916828 - Gate of the Gods

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Grand Palace of Hu'Xzoi (ID: 34) |
| Block Size       | 396 bytes                        |
| Total Events     | 3                                |
| References Count | 11                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [52](#event-52)       | 0x0002       |    322 |             44 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C5A      |        7258 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0013      |          19 |
|       6 | 0x00C9      |         201 |
|       7 | 0x005E      |          94 |
|       8 | 0x0078      |         120 |
|       9 | 0x021C      |         540 |
|      10 | 0x00B4      |         180 |

## String References

- **7258**: Open the portal? [Yes./No.]

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

### Event 52

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 322 bytes |
| Instructions | 44        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 24 00 80 01  80 02 80 25 02 00 10 02     .$......%....
0010: 80 00 30 01 43 00 43 01  46 01 42 45 03 80 F0 FF  ..0.C.C.F.BE....
0020: FF 7F F0 FF FF 7F 66 64  6F 31 02 80 1C 04 80 38  ......fdo1.....8
0030: 05 80 45 03 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
0040: 6E 02 80 45 06 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  n..E..........bl
0050: 6F 6E 02 80 45 07 80 F0  FF FF 7F F0 FF FF 7F 73  on..E..........s
0060: 69 6E 32 02 80 29 01 F0  FF FF 7F 03 45 03 80 F0  in2..)......E...
0070: FF FF 7F F0 FF FF 7F 66  64 69 31 02 80 1C 04 80  .......fdi1.....
0080: 1C 08 80 2D F8 FF FF 7F  F8 FF FF 7F 73 31 34 37  ...-........s147
0090: 2D F8 FF FF 7F F8 FF FF  7F 73 6E 30 31 1C 09 80  -........sn01...
00A0: 45 06 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 31 02  E..........who1.
00B0: 80 1C 04 80 45 06 80 F0  FF FF 7F F0 FF FF 7F 77  ....E..........w
00C0: 68 69 31 02 80 2D F8 FF  FF 7F F8 FF FF 7F 68 69  hi1..-........hi
00D0: 6B 64 4C 1C 08 80 27 01  F0 FF FF 7F 04 1C 0A 80  kdL...'.........
00E0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  E..........fdo1.
00F0: 80 4D 1C 04 80 45 06 80  F0 FF FF 7F F0 FF FF 7F  .M...E..........
0100: 77 68 69 31 02 80 52 07  80 F0 FF FF 7F F0 FF FF  whi1..R.........
0110: 7F 73 69 6E 32 45 03 80  F0 FF FF 7F F0 FF FF 7F  .sin2E..........
0120: 62 6C 6F 66 02 80 03 01  10 01 80 46 00 01 40 01  blof.......F..@.
0130: 02 00 10 01 80 00 40 01  03 01 10 02 80 01 40 01  ......@.......@.
0140: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x24] CREATE_DIALOG(message_id=7258*, default_option=1*, option_flags=0*)
    → "Open the portal? [Yes./No.]"
  2: 0x000B [0x25] WAIT_DIALOG_SELECT()
  3: 0x000C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0130
  4: 0x0014 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0016 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0018 [0x46] CAMERA_CONTROL: Disable user control
  7: 0x001A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x001B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x002C [0x1C] WAIT(60* ticks)
 10: 0x002F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 11: 0x0032 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0043 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 13: 0x0054 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sin2" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 14: 0x0065 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 15: 0x006C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x007D [0x1C] WAIT(60* ticks)
 17: 0x0080 [0x1C] WAIT(120* ticks)
 18: 0x0083 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s147" with entities [EventEntity, EventEntity]
 19: 0x0090 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "sn01" with entities [EventEntity, EventEntity]
 20: 0x009D [0x1C] WAIT(540* ticks)
 21: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 22: 0x00B1 [0x1C] WAIT(60* ticks)
 23: 0x00B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 24: 0x00C5 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "hikd" with entities [EventEntity, EventEntity]
 25: 0x00D2 [0x4C] EventEntity->StatusEvent = 8 // Open door
 26: 0x00D3 [0x1C] WAIT(120* ticks)
 27: 0x00D6 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 28: 0x00DD [0x1C] WAIT(180* ticks)
 29: 0x00E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x00F1 [0x4D] EventEntity->StatusEvent = 9 // Close door
 31: 0x00F2 [0x1C] WAIT(60* ticks)
 32: 0x00F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 33: 0x0106 [0x52] END_LOAD_SCHEDULER: End scheduler "sin2" with entities [LocalPlayer, LocalPlayer], work=94*
 34: 0x0115 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 35: 0x0126 [0x03] Work_Zone[1] = 1*
 36: 0x012B [0x46] CAMERA_CONTROL: Restore default settings
 37: 0x012D [0x01] GOTO 0x0140
 38: 0x0130 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0140
 39: 0x0138 [0x03] Work_Zone[1] = 0*
 40: 0x013D [0x01] GOTO 0x0140

SUBROUTINE_0140:
 41: 0x0140 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 42: 0x0142 [0x21] END_EVENT
 43: 0x0143 [0x00] END_REQSTACK()
```
