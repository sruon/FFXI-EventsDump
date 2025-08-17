# 17613221 - Cermet Door

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 192 bytes         |
| Total Events     | 6                 |
| References Count | 8                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [11](#event-11)       | 0x0001       |     54 |             12 |
| [12](#event-12)       | 0x0037       |     61 |             13 |
| [13](#event-13)       | 0x0074       |      1 |              1 |
| [14](#event-14)       | 0x0075       |      1 |              1 |
| [22](#event-22)       | 0x0076       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFD2F4C  |  4294782796 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x0000      |           0 |
|       4 | 0x0004      |           4 |
|       5 | 0x0028      |          40 |
|       6 | 0x00C8      |         200 |
|       7 | 0x003C      |          60 |

## String References

- **1**: The door seems to be locked from the other side.
- **2**: Pass through the door? [Yes./No.]

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 54 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    3B F0 FF FF 7F 00 00  01 00 02 00 02 00 00 00   ;..............
0010: 80 02 1B 00 48 01 80 23  01 35 00 24 02 80 03 80  ....H..#.5.$....
0020: 03 80 25 02 00 10 03 80  00 35 00 29 03 A5 C1 0C  ..%......5.)....
0030: 01 02 01 35 00 21 00                              ...5.!.         
```

#### Opcodes

```
  0: 0x0001 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x000C [0x02] IF !(ExtData[1]->WorkLocal[0] <= 4294782796*) GOTO 0x001B
  2: 0x0014 [0x48] [System] [1*]:
    → "The door seems to be locked from the other side."
  3: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0018 [0x01] GOTO 0x0035
  5: 0x001B [0x24] CREATE_DIALOG(message_id=2*, default_option=0*, option_flags=0*)
    → "Pass through the door? [Yes./No.]"
  6: 0x0022 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0023 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0035
  8: 0x002B [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Cermet Door (ID: 17613221/0x010CC1A5), tag_num=0x02)
  9: 0x0032 [0x01] GOTO 0x0035

SUBROUTINE_0035:
 10: 0x0035 [0x21] END_EVENT
 11: 0x0036 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 61 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      42  43 00 43 01 38 04 80 4C         BC.C.8..L
0040: 1C 05 80 45 06 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0050: 6F 31 03 80 1C 07 80 29  03 F0 FF FF 7F 0B 45 06  o1.....)......E.
0060: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 03 80 4D  .........fdi1..M
0070: 1C 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0037 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0038 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x003A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x003C [0x38] SET_CLIENT_EVENT_MODE(mode=4*)
  4: 0x003F [0x4C] EventEntity->StatusEvent = 8 // Open door
  5: 0x0040 [0x1C] WAIT(40* ticks)
  6: 0x0043 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x0054 [0x1C] WAIT(60* ticks)
  8: 0x0057 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x0B)
  9: 0x005E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x006F [0x4D] EventEntity->StatusEvent = 9 // Close door
 11: 0x0070 [0x1C] WAIT(60* ticks)
 12: 0x0073 [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             00                                        .           
```

#### Opcodes

```
  0: 0x0074 [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0075  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                00                                      .          
```

#### Opcodes

```
  0: 0x0075 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0076  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   00                                    .         
```

#### Opcodes

```
  0: 0x0076 [0x00] END_REQSTACK()
```
