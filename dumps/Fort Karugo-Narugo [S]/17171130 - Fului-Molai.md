# 17171130 - Fului-Molai

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 156 bytes                       |
| Total Events     | 3                               |
| References Count | 8                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [212](#event-212)     | 0x0001       |     46 |             12 |
| [110](#event-110)     | 0x002F       |     46 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0015      |          21 |
|       2 | 0x1FF5      |        8181 |
|       3 | 0x1FF6      |        8182 |
|       4 | 0x1FF7      |        8183 |
|       5 | 0x1FF8      |        8184 |
|       6 | 0x1FF9      |        8185 |
|       7 | 0x1FFA      |        8186 |

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

### Event 212

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 46 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 6E F8 FF FF 7F 01 80   ........n......
0010: 99 F8 FF FF 7F 2B F8 FF  FF 7F 02 80 23 2B F8 FF  .....+......#+..
0020: FF 7F 03 80 23 2B F8 FF  FF 7F 04 80 23 21 00     ....#+......#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x6E] EventEntity uses emote 21*
  3: 0x0010 [0x99] Wait for EventEntity animation to complete
  4: 0x0015 [0x2B] EventEntity [8181*]:
    → "Ah! An intruder! ...Oh, don't scare me like that. Look at me getting all worked up by a wandering adventurer."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x2B] EventEntity [8182*]:
    → "The three nations had their rivalries and disputes long before this madness began. Just because the allied forces are now falling into formation doesn't mean we're going to start getting along all of a sudden."
  7: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0025 [0x2B] EventEntity [8183*]:
    → "Especially Windurst and San d'Oria. We have a tradition of bad blood between us..."
  9: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002D [0x21] END_EVENT
 11: 0x002E [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 46 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1E                 .
0030: F0 FF FF 7F 1C 00 80 6E  F8 FF FF 7F 01 80 99 F8  .......n........
0040: FF FF 7F 2B F8 FF FF 7F  05 80 23 2B F8 FF FF 7F  ...+......#+....
0050: 06 80 23 2B F8 FF FF 7F  07 80 23 21 00           ..#+......#!.   
```

#### Opcodes

```
  0: 0x002F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0034 [0x1C] WAIT(30* ticks)
  2: 0x0037 [0x6E] EventEntity uses emote 21*
  3: 0x003E [0x99] Wait for EventEntity animation to complete
  4: 0x0043 [0x2B] EventEntity [8184*]:
    → "The San d'Orian Royal Knights have pried the fort from the claws of the Yagudo! Tales of their bravery will be told for a hundred years to come!"
  5: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004B [0x2B] EventEntity [8185*]:
    → "I always thought of the Elvaan as a selfish, haughty people. I guess I was wrong..."
  7: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0053 [0x2B] EventEntity [8186*]:
    → "This battle will be the turning point for the Allied Forces of Altana. You mark my words!"
  9: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x005B [0x21] END_EVENT
 11: 0x005C [0x00] END_REQSTACK()
```
