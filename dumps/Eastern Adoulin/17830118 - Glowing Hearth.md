# 17830118 - Glowing Hearth

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 204 bytes                 |
| Total Events     | 8                         |
| References Count | 10                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [540](#event-540)        | 0x0001       |     13 |              7 |
| [586](#event-586)        | 0x000E       |      1 |              1 |
| [5238](#event-5238)      | 0x000F       |      1 |              1 |
| [5239](#event-5239)      | 0x0010       |      1 |              1 |
| [5240](#event-5240)      | 0x0011       |      1 |              1 |
| [65535.1](#event-655351) | 0x0012       |     22 |              8 |
| [584](#event-584)        | 0x0028       |     76 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x28EB      |       10475 |
|       1 | 0x000D      |          13 |
|       2 | 0xFFFF57C2  |  4294924226 |
|       3 | 0xD175      |       53621 |
|       4 | 0xFFFFFF6C  |  4294967148 |
|       5 | 0x0000      |           0 |
|       6 | 0x28EC      |       10476 |
|       7 | 0x28EF      |       10479 |
|       8 | 0x00C8      |         200 |
|       9 | 0x0001      |           1 |

## String References

- **10475**: Get lost, commoner.
- **10476**: ...Welcome to the Silver Knife.
- **10479**: Enter the premises? [Of course, it's my right./No, it's not worth my attention.]

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

### Event 540

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=10475*)
    → "Get lost, commoner."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 586

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            00                   . 
```

#### Opcodes

```
  0: 0x000E [0x00] END_REQSTACK()
```

### Event 5238

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 5239

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 5240

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       32 01 80 1F 00 02  80 03 80 04 80 1F 01 6F    2............o
0020: 1E 62 11 10 01 6F 70 00                           .b...op.        
```

#### Opcodes

```
  0: 0x0012 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=-43.070*, Z=53.621*, Y=-0.148*
  2: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0020 [0x1E] EventEntity looks at Oshasha (ID: 17830242/0x01101162) and starts talking
  5: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0026 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0027 [0x00] END_REQSTACK()
```

### Event 584

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 76 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          03 01 10 05 80 1E F0 FF          ........
0030: FF 7F 6F 70 1D 06 80 23  24 07 80 05 80 05 80 25  ..op...#$......%
0040: 02 00 10 05 80 00 72 00  42 45 08 80 F0 FF FF 7F  ......r.BE......
0050: F0 FF FF 7F 66 64 6F 31  05 80 55 08 80 F0 FF FF  ....fdo1..U.....
0060: 7F F0 FF FF 7F 66 64 6F  31 03 01 10 09 80 30 01  .....fdo1.....0.
0070: 72 00 21 00                                       r.!.            
```

#### Opcodes

```
  0: 0x0028 [0x03] Work_Zone[1] = 0*
  1: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0033 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=10476*)
    → "...Welcome to the Silver Knife."
  5: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0038 [0x24] CREATE_DIALOG(message_id=10479*, default_option=0*, option_flags=0*)
    → "Enter the premises? [Of course, it's my right./No, it's not worth my attention.]"
  7: 0x003F [0x25] WAIT_DIALOG_SELECT()
  8: 0x0040 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0072
  9: 0x0048 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0049 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x005A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 12: 0x0069 [0x03] Work_Zone[1] = 1*
 13: 0x006E [0x30] SET_UCOFF_CONTINUE_ZERO()
 14: 0x006F [0x01] GOTO 0x0072

SUBROUTINE_0072:
 15: 0x0072 [0x21] END_EVENT
 16: 0x0073 [0x00] END_REQSTACK()
```
