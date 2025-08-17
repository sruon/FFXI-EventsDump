# 17171124 - Fekko-Krakko

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 100 bytes                       |
| Total Events     | 2                               |
| References Count | 4                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [206](#event-206)     | 0x0001       |     56 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0031      |          49 |
|       2 | 0x1FCE      |        8142 |
|       3 | 0x1FCF      |        8143 |

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

### Event 206

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  2B F8 FF FF 7F 02 80 23  ....tlk0+......#
0020: 2B F8 FF FF 7F 03 80 23  66 01 80 F8 FF FF 7F F8  +......#f.......
0030: FF FF 7F 74 6C 6B 31 21  00                       ...tlk1!.       
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  3: 0x0018 [0x2B] EventEntity [8142*]:
    → "Our Warlock Warlord sometimes ventures out on his own to gather intelligence on the enemy's movements."
  4: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0020 [0x2B] EventEntity [8143*]:
    → "He says that in these times we must do what we can for the Federation, and endure any hardships. He is truly an inspiration."
  6: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  8: 0x0037 [0x21] END_EVENT
  9: 0x0038 [0x00] END_REQSTACK()
```
