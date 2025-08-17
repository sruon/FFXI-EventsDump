# 17801246 - Shark Teeth

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 120 bytes        |
| Total Events     | 5                |
| References Count | 7                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [119](#event-119)        | 0x0001       |     15 |              8 |
| [120](#event-120)        | 0x0010       |     19 |             10 |
| [121](#event-121)        | 0x0023       |     11 |              2 |
| [65535.1](#event-655351) | 0x002E       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2711      |       10001 |
|       1 | 0x2712      |       10002 |
|       2 | 0x2713      |       10003 |
|       3 | 0xFFFFFE39  |  4294966841 |
|       4 | 0xFFFFC57B  |  4294952315 |
|       5 | 0xFFFFF060  |  4294963296 |
|       6 | 0x086E      |        2158 |

## String References

- **10001**: Hey! Don't take one more step. You're not going anywhere until you get checked by Dakha Topsalwan.
- **10002**: You can't come in here! This is the airship arrivals gate.
- **10003**: If you are ready to depart Kazham, pay the boarding fee at the counter on the other side.

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

### Event 119

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 20 00 21 00   .....op...# .!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=10001*)
    → "Hey! Don't take one more step. You're not going anywhere until you get checked by Dakha Topsalwan."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x000E [0x21] END_EVENT
  7: 0x000F [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1E F0 FF FF 7F 6F 70 1D  01 80 23 1D 02 80 23 20  .....op...#...# 
0020: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0016 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10002*)
    → "You can't come in here! This is the airship arrivals gate."
  4: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=10003*)
    → "If you are ready to depart Kazham, pay the boarding fee at the counter on the other side."
  6: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0021 [0x21] END_EVENT
  9: 0x0022 [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 11 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          79 00 1D A0 0F  01 F0 FF FF 7F 00           y..........  
```

#### Opcodes

```
  0: 0x0023 [0x79] Flame Walker (ID: 17801245/0x010FA01D) looks at LocalPlayer (Basic look)
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            37 03                7.
0030: 80 04 80 05 80 06 80 00                           ........        
```

#### Opcodes

```
  0: 0x002E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.455*, z=-14.981*, y=-4.000*, direction=189.7°*
  1: 0x0037 [0x00] END_REQSTACK()
```
