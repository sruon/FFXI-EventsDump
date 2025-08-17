# 17396214 - Kaa Toru the Just

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Castle Oztroja (ID: 151) |
| Block Size       | 164 bytes                |
| Total Events     | 8                        |
| References Count | 7                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      5 |              3 |
| [45](#event-45)          | 0x0006       |     40 |             11 |
| [65535.2](#event-655352) | 0x002E       |      5 |              3 |
| [65535.3](#event-655353) | 0x0033       |      5 |              3 |
| [65535.4](#event-655354) | 0x0038       |      5 |              3 |
| [65535.5](#event-655355) | 0x003D       |      5 |              3 |
| [46](#event-46)          | 0x0042       |     19 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D20      |        7456 |
|       1 | 0x1D21      |        7457 |
|       2 | 0x1D22      |        7458 |
|       3 | 0x1D23      |        7459 |
|       4 | 0x1D24      |        7460 |
|       5 | 0x1D25      |        7461 |
|       6 | 0x1D26      |        7462 |

## String References

- **7456**: If you hop down here, you be finding shortcut to the entrance of Castle Oztroja.
- **7457**: I am Kaa Toru the Just.
- **7458**: You be the victor of Balga Contest held in Giddeus, kyah? You be taking this $3 and your prize.
- **7459**: This contest being beneficial for both Yagudo and smoothskins. Valuable knowledge and skills be exchanged.
- **7460**: Quawk! You be going back to your nest now. Your victory be the most valuable thing you taking with you.
- **7461**: ...Kyah! Now what you be wanting? Quawk? You saying you had hard time getting here?
- **7462**: Not words me be expecting from champion of Balga Contest, kyah! Victor has a duty to be meeting all challenges. A duty of the just.

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 00                                  ...#.          
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7456*)
    → "If you hop down here, you be finding shortcut to the entrance of Castle Oztroja."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 45

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 40 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   42 1E  F0 FF FF 7F 6F 70 29 0B        B.....op).
0010: F6 71 09 01 03 29 0B F6  71 09 01 04 29 0B F6 71  .q...)..q...)..q
0020: 09 01 05 29 0B F6 71 09  01 06 20 00 21 00        ...)..q... .!.  
```

#### Opcodes

```
  0: 0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0007 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kaa Toru the Just (ID: 17396214/0x010971F6), tag_num=0x03)
  5: 0x0015 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kaa Toru the Just (ID: 17396214/0x010971F6), tag_num=0x04)
  6: 0x001C [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kaa Toru the Just (ID: 17396214/0x010971F6), tag_num=0x05)
  7: 0x0023 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kaa Toru the Just (ID: 17396214/0x010971F6), tag_num=0x06)
  8: 0x002A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x002C [0x21] END_EVENT
 10: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            1D 01                ..
0030: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7457*)
    → "I am Kaa Toru the Just."
  1: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0033  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          1D 02 80 23 00                              ...#.        
```

#### Opcodes

```
  0: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=7458*)
    → "You be the victor of Balga Contest held in Giddeus, kyah? You be taking this $3 and your prize."
  1: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0038  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          1D 03 80 23 00                   ...#.   
```

#### Opcodes

```
  0: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=7459*)
    → "This contest being beneficial for both Yagudo and smoothskins. Valuable knowledge and skills be exchanged."
  1: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003D  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1D 04 80               ...
0040: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=7460*)
    → "Quawk! You be going back to your nest now. Your victory be the most valuable thing you taking with you."
  1: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0041 [0x00] END_REQSTACK()
```

### Event 46

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       1E F0 FF FF 7F 6F  70 1D 05 80 23 1D 06 80    .....op...#...
0050: 23 20 00 21 00                                    # .!.           
```

#### Opcodes

```
  0: 0x0042 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0048 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=7461*)
    → "...Kyah! Now what you be wanting? Quawk? You saying you had hard time getting here?"
  4: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7462*)
    → "Not words me be expecting from champion of Balga Contest, kyah! Victor has a duty to be meeting all challenges. A duty of the just."
  6: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0051 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0053 [0x21] END_EVENT
  9: 0x0054 [0x00] END_REQSTACK()
```
