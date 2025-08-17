# 17760336 - Peepikiki

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 140 bytes               |
| Total Events     | 6                       |
| References Count | 3                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     16 |              2 |
| [65535.3](#event-655353) | 0x0021       |     16 |              2 |
| [65535.4](#event-655354) | 0x0031       |      9 |              3 |
| [359](#event-359)        | 0x003A       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1023      |        4131 |

## String References

- **4131**: Hmm...I wonder what things foreigners like to buy?

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   f..........thk1
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   f..........thk2
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0021 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0031  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0031 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0036 [0x1C] WAIT(30* ticks)
  2: 0x0039 [0x00] END_REQSTACK()
```

### Event 359

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                1E F0 FF FF 7F 6F            .....o
0040: 70 29 0B 50 00 0F 01 02  1D 02 80 23 29 0B 50 00  p).P.......#).P.
0050: 0F 01 03 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x003A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0040 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0041 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Peepikiki (ID: 17760336/0x010F0050), tag_num=0x02)
  4: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=4131*)
    → "Hmm...I wonder what things foreigners like to buy?"
  5: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004C [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Peepikiki (ID: 17760336/0x010F0050), tag_num=0x03)
  7: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0055 [0x21] END_EVENT
  9: 0x0056 [0x00] END_REQSTACK()
```
