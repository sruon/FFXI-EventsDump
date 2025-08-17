# 17969914 - Etched Rock

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Reisenjima (ID: 291) |
| Block Size       | 328 bytes            |
| Total Events     | 2                    |
| References Count | 15                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [11](#event-11)       | 0x0001       |    241 |             31 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1CDF      |        7391 |
|       2 | 0x0001      |           1 |
|       3 | 0x00C8      |         200 |
|       4 | 0x001B      |          27 |
|       5 | 0x3F6A5     |      259749 |
|       6 | 0xDEEE      |       57070 |
|       7 | 0xFFFEAB2F  |  4294880047 |
|       8 | 0x03F7      |        1015 |
|       9 | 0x0301      |         769 |
|      10 | 0x000F      |          15 |
|      11 | 0x00B4      |         180 |
|      12 | 0x00AD      |         173 |
|      13 | 0x0046      |          70 |
|      14 | 0x0014      |          20 |

## String References

- **7391**: Enter the sanctorium? [Yes./No.]

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

### Event 11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 241 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 01 10 00 80 24 01  80 02 80 00 80 25 02 00   .....$......%..
0010: 10 00 80 00 F0 00 43 00  43 01 42 45 03 80 F0 FF  ......C.C.BE....
0020: FF 7F F0 FF FF 7F 66 64  6F 31 00 80 55 03 80 F0  ......fdo1..U...
0030: FF FF 7F F0 FF FF 7F 66  64 6F 31 46 01 38 04 80  .......fdo1F.8..
0040: BA F0 FF FF 7F 05 80 06  80 07 80 08 80 80 F0 FF  ................
0050: FF 7F 45 09 80 F8 FF FF  7F F8 FF FF 7F 73 30 38  ..E..........s08
0060: 31 00 80 1C 0A 80 45 03  80 F0 FF FF 7F F0 FF FF  1.....E.........
0070: 7F 66 64 69 31 00 80 1C  0B 80 52 09 80 F8 FF FF  .fdi1.....R.....
0080: 7F F8 FF FF 7F 73 30 38  31 45 09 80 F8 FF FF 7F  .....s081E......
0090: F8 FF FF 7F 73 30 38 32  00 80 D0 0C 80 F0 FF FF  ....s082........
00A0: 7F F0 FF FF 7F 73 30 30  30 00 80 1C 0D 80 92 01  .....s000.......
00B0: F0 FF FF 7F 1C 0E 80 45  03 80 F0 FF FF 7F F0 FF  .......E........
00C0: FF 7F 66 64 6F 31 00 80  55 03 80 F0 FF FF 7F F0  ..fdo1..U.......
00D0: FF FF 7F 66 64 6F 31 52  09 80 F8 FF FF 7F F8 FF  ...fdo1R........
00E0: FF 7F 73 30 38 32 46 00  03 01 10 02 80 01 F0 00  ..s082F.........
00F0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[1] = 0*
  1: 0x0006 [0x24] CREATE_DIALOG(message_id=7391*, default_option=1*, option_flags=0*)
    → "Enter the sanctorium? [Yes./No.]"
  2: 0x000D [0x25] WAIT_DIALOG_SELECT()
  3: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F0
  4: 0x0016 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0018 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x001A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x001B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x002C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  9: 0x003B [0x46] CAMERA_CONTROL: Disable user control
 10: 0x003D [0x38] SET_CLIENT_EVENT_MODE(mode=27*)
 11: 0x0040 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=259.749*, pos_z=57.070*, pos_y=-87.249*, direction=89.2°*)
 12: 0x004D [0x80] LOAD_WAIT(entity=LocalPlayer)
 13: 0x0052 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s081" with entities [EventEntity, EventEntity], work=[769*, 0*]
 14: 0x0063 [0x1C] WAIT(15* ticks)
 15: 0x0066 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0077 [0x1C] WAIT(180* ticks)
 17: 0x007A [0x52] END_LOAD_SCHEDULER: End scheduler "s081" with entities [EventEntity, EventEntity], work=769*
 18: 0x0089 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s082" with entities [EventEntity, EventEntity], work=[769*, 0*]
 19: 0x009A [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "s000" with entities [LocalPlayer, LocalPlayer], work=[173*, 0*]
 20: 0x00AB [0x1C] WAIT(70* ticks)
 21: 0x00AE [0x92] LocalPlayer->Render.Flags3 ^= 0x01
 22: 0x00B4 [0x1C] WAIT(20* ticks)
 23: 0x00B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x00C8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 25: 0x00D7 [0x52] END_LOAD_SCHEDULER: End scheduler "s082" with entities [EventEntity, EventEntity], work=769*
 26: 0x00E6 [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x00E8 [0x03] Work_Zone[1] = 1*
 28: 0x00ED [0x01] GOTO 0x00F0

SUBROUTINE_00F0:
 29: 0x00F0 [0x21] END_EVENT
 30: 0x00F1 [0x00] END_REQSTACK()
```
