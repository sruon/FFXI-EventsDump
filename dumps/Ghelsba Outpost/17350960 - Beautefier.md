# 17350960 - Beautefier

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ghelsba Outpost (ID: 140) |
| Block Size       | 144 bytes                 |
| Total Events     | 4                         |
| References Count | 6                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |     15 |              4 |
| [3](#event-3)            | 0x0010       |     15 |              4 |
| [65535.1](#event-655351) | 0x001F       |     56 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x004B      |          75 |
|       1 | 0x002D      |          45 |
|       2 | 0x000B      |          11 |
|       3 | 0xFFFD6A26  |  4294797862 |
|       4 | 0x11B22     |       72482 |
|       5 | 0xFFFFD268  |  4294955624 |

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

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 92 01 F8 FF FF 7F 00   "./............
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 22 00 2F 00 F8 FF FF 7F  92 01 F8 FF FF 7F 00     "./............ 
```

#### Opcodes

```
  0: 0x0010 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0012 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0018 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 56 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 73 69 74 31 53 F8  ..........sit1S.
0030: FF FF 7F F8 FF FF 7F 73  69 74 31 1C 01 80 32 02  .......sit1...2.
0040: 80 1F 00 03 80 04 80 05  80 1F 01 6F 79 00 F8 FF  ...........oy...
0050: FF 7F 31 C1 08 01 00                              ..1....         
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sit1" with entities [EventEntity, EventEntity], work=75*
  1: 0x002E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit1" with entities [EventEntity, EventEntity]
  2: 0x003B [0x1C] WAIT(45* ticks)
  3: 0x003E [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  4: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=-169.434*, Z=72.482*, Y=-11.672*
  5: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x004C [0x79] EventEntity looks at Vaseradoul (ID: 17350961/0x0108C131) (Basic look)
  8: 0x0056 [0x00] END_REQSTACK()
```
