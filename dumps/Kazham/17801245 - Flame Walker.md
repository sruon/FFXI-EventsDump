# 17801245 - Flame Walker

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 112 bytes        |
| Total Events     | 5                |
| References Count | 6                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [117](#event-117)        | 0x0001       |     15 |              8 |
| [118](#event-118)        | 0x0010       |     15 |              8 |
| [116](#event-116)        | 0x001F       |     11 |              2 |
| [65535.1](#event-655351) | 0x002A       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x270B      |        9995 |
|       1 | 0x270C      |        9996 |
|       2 | 0xFFFFB472  |  4294947954 |
|       3 | 0xFFFFCF2F  |  4294954799 |
|       4 | 0xFFFFF061  |  4294963297 |
|       5 | 0x011A      |         282 |

## String References

- **9995**: You want to enter Kazham? Look at the sign, buddy. This is the departures gate. The arrivals gate is on the other side.
- **9996**: Pay your boarding fee to Bhoyu Halpatacco at the counter there.

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

### Event 117

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
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=9995*)
    → "You want to enter Kazham? Look at the sign, buddy. This is the departures gate. The arrivals gate is on the other side."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x000E [0x21] END_EVENT
  7: 0x000F [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1E F0 FF FF 7F 6F 70 1D  01 80 23 20 00 21 00     .....op...# .!. 
```

#### Opcodes

```
  0: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0016 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9996*)
    → "Pay your boarding fee to Bhoyu Halpatacco at the counter there."
  4: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 11 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               79                 y
0020: 00 1D A0 0F 01 F0 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x001F [0x79] Flame Walker (ID: 17801245/0x010FA01D) looks at LocalPlayer (Basic look)
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                37 02 80 03 80 04            7.....
0030: 80 05 80 00                                       ....            
```

#### Opcodes

```
  0: 0x002A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-19.342*, z=-12.497*, y=-3.999*, direction=24.8°*
  1: 0x0033 [0x00] END_REQSTACK()
```
